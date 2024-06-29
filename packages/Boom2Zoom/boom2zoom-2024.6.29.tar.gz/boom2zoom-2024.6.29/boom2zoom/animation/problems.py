from __future__ import annotations

from enum import Flag, auto
from typing import Container

from .boom import BoomSwitch, BoomAnimation


class BoomProblems(Flag):
    """Represents problems with SWITCH/ANIMATED records.

    Implemented as an enum.Flag subclass.
    """

    def pretty(self) -> str:
        """Human-friendly representation of this set of problems."""
        return " | ".join(name.replace("_", " ") for name in self._get_names())

    def _get_names(self) -> list[str]:
        """Returns the names of the flags which are set."""
        return [flag.name for flag in type(self) if flag in self and flag.name is not None]


class AnimatedProblems(BoomProblems):
    duplicate_names = auto()
    zero_tics = auto()
    first_not_found = auto()
    last_not_found = auto()

    def _get_names(self) -> list[str]:
        names = super()._get_names()
        if "first_not_found" and "last_not_found" in names:
            names.remove("first_not_found")
            names.remove("last_not_found")
            names.insert(0, "frames not found")
        return names


class SwitchProblems(BoomProblems):
    duplicate_names = auto()
    on_not_found = auto()
    off_not_found = auto()


def validate_switch_in_context(switch: BoomSwitch, textures: Container[str]) -> SwitchProblems:
    problems = SwitchProblems(0)

    if switch.on == switch.off:
        problems |= SwitchProblems.duplicate_names

    if switch.on not in textures:
        problems |= SwitchProblems.on_not_found

    if switch.off not in textures:
        problems |= SwitchProblems.off_not_found

    return problems


def validate_animation_in_context(
    record: BoomAnimation,
    textures: Container[str],
    flats: Container[str],
) -> AnimatedProblems:
    """Validates the given *animated* record and returns its associated problems."""
    problems = AnimatedProblems(0)

    if record.first == record.last:
        problems |= AnimatedProblems.duplicate_names

    if record.tics == 0:
        problems |= AnimatedProblems.zero_tics

    search_space = textures if record.is_wall else flats

    if record.first not in search_space:
        problems |= AnimatedProblems.first_not_found

    if record.last not in search_space:
        problems |= AnimatedProblems.last_not_found

    return problems
