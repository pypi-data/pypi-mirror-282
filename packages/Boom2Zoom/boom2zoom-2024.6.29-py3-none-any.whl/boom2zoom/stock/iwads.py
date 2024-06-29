"""Database on official IWADS."""

from __future__ import annotations

from functools import cache

from attr import frozen

from boom2zoom.settings import GAMES_PATH
from boom2zoom.utils import load_csv


@frozen
class IWadInfo:
    crc: int
    title: str
    note: str

    def __str__(self):
        return f"IwadInfo({self.title}, {self.note} [{self.crc:X}])"


@cache
def get_iwads() -> list[IWadInfo]:
    """Returns known IWads as IWadInfo records."""
    rows = load_csv(GAMES_PATH)
    return [
        IWadInfo(
            crc=int(row["crc"], 16),
            title=row["title"],
            note=row["note"],
        )
        for row in rows
    ]
