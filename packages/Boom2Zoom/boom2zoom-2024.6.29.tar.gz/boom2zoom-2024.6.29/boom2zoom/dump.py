from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from omg import WAD
from rich.console import Console
from rich.progress import track
from rich.prompt import Confirm

from boom2zoom.animation import (
    get_switches,
    get_animated,
    to_animdefs,
    expand_animation,
    validate_switch_in_context,
    validate_animation_in_context,
)
from .stock import BOOM_DEFAULT_SWITCHES, STOCK_ANIMATED
from .textures import (
    get_textures,
    get_flats,
    make_patch_lookup,
    render_texture,
    check_have_patches,
    image_is_stock_texture,
)
from .utils import p, save_image_to_png


def dump(
    wad: WAD,
    supporting: Sequence[WAD],
    dest: Path,
    animdefs_in_full: bool,
    prompt_for_continue: bool,
    check_ip: bool,
) -> None:
    """Export a Wad's assets to a directory."""

    ## GET READY

    # nothing special about where flats and texture definitions come from
    flats = get_flats(wad)
    textures = get_textures(wad)

    # patches come from the main wad and supporting wads
    patches = make_patch_lookup(wad, *supporting)

    # For both SWITCHES and ANIMATED, we only care about unique, non-stock records upfront.
    switches = set(get_switches(wad)) - BOOM_DEFAULT_SWITCHES
    animated = set(get_animated(wad)) - STOCK_ANIMATED

    ## VALIDATION

    # For switches and animations, we map each record to its problems.
    loose_switches = {
        switch: problems
        for switch in switches
        if (problems := validate_switch_in_context(switch, textures))
    }

    busted_animations = {
        animation: problems
        for animation in animated
        if (problems := validate_animation_in_context(animation, textures, flats))
    }

    # Textures just have missing patches.
    patchy_textures = [
        txname for txname, txdef in textures.items() if not check_have_patches(txdef, patches)
    ]

    if loose_switches:
        print("These SWITCH entries have problems:")
        for switch, problems in loose_switches.items():
            print(f"{switch.summary()} -> {problems.pretty()}")
        print()

    if busted_animations:
        print("These ANIMATED records have problems:")
        for record, problems in busted_animations.items():
            print(f"{record.summary()} -> {problems.pretty()}")
        print()

    if patchy_textures:
        preview = patchy_textures[:6]
        patches_txt = ", ".join(preview)
        if len(preview) < len(patchy_textures):
            patches_txt += f"... and {len(patchy_textures) - len(preview)} more."
        Console().print(
            f"The follow textures are missing patches: {patches_txt}\n\n"
            "Did you forget to add a base wad with --base ?\n"
        )

    ## CONTINUE?

    there_are_problems = loose_switches or busted_animations or patchy_textures

    if prompt_for_continue and there_are_problems:
        if not Confirm.ask("Continue?"):
            raise SystemExit(0)

    if not there_are_problems:
        print("No problems were found.\n")

    # REMOVE INVALIDS

    switches -= set(loose_switches)
    animated -= set(busted_animations)
    for name in patchy_textures:
        del textures[name]

    ## ANIMDEFS
    animation_groups = []

    if switches:
        animation_groups.append(switches)

    if animdefs_in_full:
        texture_names = list(textures)
        flat_names = list(flats)
        texture_animations = [expand_animation(x, texture_names, flat_names) for x in animated]
    else:
        texture_animations = animated

    if texture_animations:
        animation_groups.append(texture_animations)

    if animation_groups:
        animdefs_txt = "\n\n".join(to_animdefs(x) for x in animation_groups).strip()

        animdefs_path = dest / "ANIMDEFS.txt"
        dest.mkdir(parents=True, exist_ok=True)

        animdefs_path.touch()
        animdefs_path.write_text(animdefs_txt)

    ## EXPORT TEXTURES
    num_stock_textures = 0
    if textures:
        progress_bar_textures = track(textures.items(), description="Exporting textures...")

        for (
            texture_name,
            texture_def,
        ) in progress_bar_textures:  # pyright: ignore[reportUnknownVariableType]
            img = render_texture(texture_def, patches)

            if check_ip and image_is_stock_texture(img):
                num_stock_textures += 1
                continue

            save_image_to_png(
                img,
                dest / "textures" / f"{texture_name}.png",
            )

    ## EXPORT FLATS
    if flats:
        progress_bar_flats = track(flats.items(), description="Exporting flats......")
        for (
            flat_name,
            flat_lump,
        ) in progress_bar_flats:  # pyright: ignore[reportUnknownVariableType]
            save_image_to_png(
                flat_lump.to_Image("RGBA"),
                dest / "flats" / f"{flat_name}.png",
            )

        print()

    num_textures = len(textures) - num_stock_textures
    num_flats = len(flats)
    num_animations = sum(len(group) for group in animation_groups)

    print(
        f"Exported "
        f"{num_textures} {p('texture', num_textures)}, "
        f"{num_flats} {p('flat', num_flats)}, "
        f"and {num_animations} animation {p('definition', num_animations)}."
    )
    if num_stock_textures:
        print(f"{num_stock_textures} stock {p('texture', num_stock_textures)} were skipped.")
