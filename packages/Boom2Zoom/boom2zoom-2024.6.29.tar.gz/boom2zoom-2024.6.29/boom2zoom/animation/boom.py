from collections.abc import Iterator
from enum import Enum
from typing import NamedTuple

SWITCHES_ROW_SIZE = 20
ANIMATED_ROW_SIZE = 23


class AnimatedType(Enum):
    FLAT = 0
    WALL = 1
    WALL_ALLOW_DECALS = 3


class BoomAnimation(NamedTuple):
    """A Boom ANIMATED entry.

    Fields are ordered the same as they are in the lump.
    """

    type: AnimatedType
    last: str
    first: str
    tics: int

    @property
    def is_wall(self) -> bool:
        """True if type is wall/allow decals."""
        return self.type in (AnimatedType.WALL, AnimatedType.WALL_ALLOW_DECALS)

    @property
    def is_flat(self) -> bool:
        """True if type is 0 (flat)."""
        return self.type == AnimatedType.FLAT

    @property
    def allowdecals(self) -> bool:
        """True if type is 3 (allow decals)."""
        return self.type == AnimatedType.WALL_ALLOW_DECALS

    def summary(self) -> str:
        return f"{self.first} -> {self.last}, {self.tics} tics, {self.type.name}"

    def __str__(self) -> str:
        return f"Animated({self.summary()})"


class BoomSwitch(NamedTuple):
    """A Boom SWITCHES entry.

    Fields are ordered the same as they are in the lump.
    """

    off: str
    on: str
    type: int

    def summary(self) -> str:
        return f"OFF: {self.off}, ON: {self.on}, Type: {self.type}"

    def __str__(self) -> str:
        return f"Switch({self.summary()})"


def decode_animated_lump(lump_data: bytes) -> Iterator[BoomAnimation]:
    """Decodes animations from a raw Boom ANIMATED lump.

    Each row from the ANIMATED lump is yielded as a `BoomAnimation`.
    """
    i = 0
    while i * ANIMATED_ROW_SIZE < len(lump_data):
        offset: int = i * ANIMATED_ROW_SIZE
        entry_type: int = lump_data[offset]

        if entry_type == 255:  # Record to mark end
            break

        last_texture: str = lump_data[offset + 1 : offset + 10].decode("ascii").rstrip("\0")
        first_texture: str = lump_data[offset + 10 : offset + 19].decode("ascii").rstrip("\0")
        animation_speed: int = int.from_bytes(lump_data[offset + 19 : offset + 23], "little")

        yield BoomAnimation(
            type=AnimatedType(entry_type),
            last=last_texture,
            first=first_texture,
            tics=animation_speed,
        )
        i += 1


def decode_switches_lump(lump_data: bytes) -> Iterator[BoomSwitch]:
    """Decodes switches from a raw Boom SWITCHES lump.

    Each row from the lump is yielded as a `BoomAnimation`.
    """
    num_entries = len(lump_data) // SWITCHES_ROW_SIZE

    for i in range(num_entries):
        offset = i * SWITCHES_ROW_SIZE
        game_type = int.from_bytes(lump_data[offset + 18 : offset + 20], "little")

        if game_type == 0:  # Reached the end
            break

        off_texture = lump_data[offset : offset + 9].decode("ascii").rstrip("\0")
        on_texture = lump_data[offset + 9 : offset + 18].decode("ascii").rstrip("\0")

        yield BoomSwitch(off=off_texture, on=on_texture, type=game_type)
