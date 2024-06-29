"""Tools for outputting ANIMDEFS syntax."""

from collections.abc import Sequence, Iterable


# REF:
# https://github.com/ZDoom/gzdoom/blob/master/src/gamedata/textures/animations.cpp
# https://zdoom.org/wiki/ANIMDEFS


# TODO: structure ANIMDEFS definitions properly, you lazy goose


def join_definitions(definitions: Iterable[str]) -> str:
    """Neatly combines ANIMDEFS definitions into one string.

    Formatting rules:
        If a definition is multiline, then it gets a one-line margin above and below. These margins collapse. Single
        lines do not get margins.
    """

    staging: list[str] = []

    for string in definitions:
        blank_behind = staging[-2::] == ["\n", "\n"]
        current_is_multiline = "\n" in string

        if current_is_multiline and not blank_behind:
            staging.append("\n")

        staging.append(string)
        staging.append("\n")

        if current_is_multiline:
            staging.append("\n")

    return "".join(staging).strip()


def format_switch(off: str, on: str) -> str:
    """Creates a SWITCH animation definition."""
    return f"SWITCH {off:<8} On Pic {on:<8} Tics 0"


def format_texture_with_range(
    first: str,
    last: str,
    tics: int,
    flat: bool = False,
    allowdecals: bool = False,
    optional: bool = True,
) -> str:
    """Creates a TEXTURE/FLAT animation definition with the RANGE command.

    Examples:
        >>> format_texture_with_range(first="NUKAGE1", last="NUKAGE3", tics=8).split()
        ['TEXTURE', 'Optional', 'NUKAGE1', 'Range', 'NUKAGE3', 'Tics', '8']

    Raises:
        ValueError: if `first` or `last` frame names are falsy, or if `tics` is less than 1.
    """

    if not first:
        raise ValueError("Need first frame.")

    if not last:
        raise ValueError("Need last frame.")

    if tics < 1:
        raise ValueError("Tics should be positive.")

    return _fmt_texture(
        flat=flat,
        name=first,
        optional=optional,
        commands=[_format_range_command(last, tics)],
        allowdecals=allowdecals,
    )


def format_texture_with_pics(
    frames: Sequence[str],
    tics: int,
    flat: bool = False,
    allowdecals: bool = False,
    optional: bool = True,
) -> str:
    """Created a TEXTURE/FLAT animation using the PIC command per frame.

    The name of the animation is the first frame.

    Examples:
        >>> format_texture_with_pics(
        ... ["FRAME1", "FRAME2", "FRAME3"],
        ... tics=5,
        ... optional=False,
        ... allowdecals=True).split()
        ['TEXTURE', 'FRAME1', 'Pic', 'FRAME1', 'Tics', '5', 'Pic', 'FRAME2', 'Tics', '5', 'Pic', 'FRAME3', 'Tics', '5', 'ALLOWDECALS']
    """

    if len(frames) < 2:
        raise ValueError(f"An animation needs at least two frames, only got {frames}.")

    for i, frame in enumerate(frames):
        if not frame:
            raise ValueError(f"Bad frame, i{i}, in sequence {frame}")

    if tics < 1:
        raise ValueError("Tics should be positive.")

    commands = [_format_pic_command(frame, tics) for frame in frames]

    return _fmt_texture(
        flat=flat, name=frames[0], commands=commands, allowdecals=allowdecals, optional=optional
    )


def _format_range_command(last: str, tics: int):
    return f"Range {last:<8} Tics {tics}"


def _format_pic_command(name: str, tics: int):
    assert name
    assert tics

    return f"Pic {name:<8} Tics {tics}"


def _fmt_texture(
    name: str,
    commands: Sequence[str],
    flat: bool = False,
    allowdecals: bool = False,
    optional: bool = False,
) -> str:
    """Low-level formatter for animated graphics in ANIMDEFS

    Output:

    TEXTURE/FLAT [Optional] <name>
        <cmd_seq>[0]
        <cmd_seq>[1]
        ...
        [ALLOWDECALS]

    where
        TEXTURE/FLAT is FLAT if *flat* else TEXTURE
        <cmd_seq> is a sequence of PIC or RANGE commands

    If there is only one command, then we format the whole definition as one line.
    """

    assert len(commands) > 0

    header = ("FLAT" if flat else "TEXTURE") + (" Optional " if optional else " ") + name

    allowdecals_txt = "ALLOWDECALS" if allowdecals else ""

    if len(commands) == 1:
        return f"{header} {commands[0]} {allowdecals_txt}"

    else:
        body = "\n  ".join(commands)
        return f"{header}\n  {body}\n  {allowdecals_txt}".rstrip()
