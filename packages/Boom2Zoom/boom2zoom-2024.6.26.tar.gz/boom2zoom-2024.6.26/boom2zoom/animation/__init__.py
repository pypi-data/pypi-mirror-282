from __future__ import annotations

from collections.abc import Iterable
from typing import TypeAlias

from omg import WAD

from . import animdefs
from .boom import *
from .expanded import *
from .problems import *

# Nuitka does not support using type builtin for aliases
AnimationLike: TypeAlias = (
    str | BoomSwitch | BoomAnimation | ExpandedBoom | Iterable["AnimationLike"]
)


def to_animdefs(x: AnimationLike) -> str:
    """Convert animation data to ANIMDEFS syntax.

    This function takes various types of animation data and converts them into a string
    formatted according to the ANIMDEFS syntax.

    Args:
        x: The animation data to convert. It can be a string, a `BoomSwitch`, a `BoomAnimation`, an `ExpandedBoom` or
        iterable of these types. We only check if *x* is iterable if it is not the other types. If iterable, each item
        in *x* is called with `to_animdefs` and the resulting ANIMDEFS strings are concatenated with
        :meth:`join_definitions`.

    Returns:
        str: The formatted ANIMDEFS string.

    Raises:
        TypeError: If the input type is not supported.
    """

    if isinstance(x, str):
        return x

    if isinstance(x, BoomSwitch):
        return animdefs.format_switch(x.off, x.on)

    if isinstance(x, BoomAnimation):
        return animdefs.format_texture_with_range(
            first=x.first,
            last=x.last,
            tics=x.tics,
            flat=x.is_flat,
            allowdecals=x.allowdecals,
        )

    if isinstance(x, ExpandedBoom):
        return animdefs.format_texture_with_pics(
            frames=x.frames,
            tics=x.record.tics,
            flat=x.record.is_flat,
            allowdecals=x.record.allowdecals,
        )

    try:
        _ = iter(x)
    except TypeError:
        raise TypeError(f"Unexpected type {type(x)}")
    else:
        return animdefs.join_definitions(to_animdefs(sub_item) for sub_item in x)


def get_animated(wad: WAD) -> list[BoomAnimation]:
    """Retrieve Boom animations from a WAD file.

    This function extracts the ANIMATED lump from a WAD file and decodes it into a list of BoomAnimation objects. If the
    WAD file does not contain an ANIMATED lump, an empty list is returned.

    Args:
        wad: The `omg.WAD` instance from which to retrieve the Boom animations.

    Returns:
        A list of BoomAnimation objects representing the animations found in the WAD file.
        If no animations are found, an empty list is returned.
    """
    if "ANIMATED" in wad.data:
        return list(decode_animated_lump(wad.data["ANIMATED"].data))
    return []


def get_switches(wad: WAD) -> list[BoomSwitch]:
    """Retrieve Boom switches from a WAD file.

    This function extracts the SWITCHES lump from a WAD file and decodes it into a list of BoomAnimation objects. If the
    WAD file does not contain an ANIMATED lump, an empty list is returned.

    Args:
        wad: The `omg.WAD` instance from which to retrieve the Boom animations.

    Returns:
        A list of BoomAnimation objects representing the animations found in the WAD file.
        If no switches are found, an empty list is returned.
    """
    if "SWITCHES" in wad.data:
        return list(decode_switches_lump(wad.data["SWITCHES"].data))
    return []
