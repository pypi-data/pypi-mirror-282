"""CLI entry point."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from omg import WAD
from typer import Option, Argument

from boom2zoom.dump import dump

app = typer.Typer(
    pretty_exceptions_enable=False,
    add_completion=False,
)


@app.command(help="Export assets from a WAD to a directory.")
def cli(
    wad_path: Annotated[
        Path,
        Argument(
            ...,
            metavar="WAD",
            help="Wad to dump",
            show_default=False,
        ),
    ],
    #
    dest: Annotated[
        Path,
        Argument(
            ...,
            help="Directory to output files - will be created if it doesn't exist.",
            show_default=False,
        ),
    ],
    #
    base: Annotated[
        list[Path],
        Option(
            default_factory=list,
            show_default=False,
            help="Extra Wad to look for patches in. Use --base again to specify even more.",
        ),
    ],
    #
    skip_ip: Annotated[
        bool,
        Option(
            ...,
            "--skip-ip-check",
            help="Don't filter out known official textures.",
        ),
    ] = False,
    #
    range_animdefs: Annotated[
        bool,
        Option(
            "--range-animdefs",
            help="Write animations just using RANGE.",
        ),
    ] = False,
    #
    assume_yes: Annotated[
        bool,
        Option(
            ...,
            "--yes",
            "-y",
            help="Assume yes to all prompts.",
        ),
    ] = False,
):
    wad = WAD(str(wad_path))
    support = [WAD(str(s)) for s in base]

    dump(
        wad,
        support,
        dest=dest,
        animdefs_in_full=not range_animdefs,
        prompt_for_continue=not assume_yes,
        check_ip=not skip_ip,
    )


if __name__ == "__main__":
    app()
