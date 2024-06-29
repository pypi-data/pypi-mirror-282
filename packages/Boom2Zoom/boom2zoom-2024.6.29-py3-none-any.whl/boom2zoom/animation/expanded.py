from __future__ import annotations

from typing import NamedTuple, Sequence, TYPE_CHECKING

from boom2zoom.utils import slice_by_indices

if TYPE_CHECKING:
    from boom2zoom.animation import BoomAnimation


class ExpandedBoom(NamedTuple):
    """A tuple of BoomAnimation with a full set of frames."""

    record: BoomAnimation
    frames: Sequence[str]


def expand_animation(
    x: BoomAnimation,
    /,
    textures: Sequence[str],
    flats: Sequence[str],
) -> ExpandedBoom:
    """Finds the full set of frame names for a Boom animation.

    The frames will be sourced from *textures* or *flats*, which must be a sequence of the available texture/flat names.

    Note: The record should be valid in context of the given textures and flats."""

    names = textures if x.is_wall else flats

    i1 = names.index(x.first)
    i2 = names.index(x.last)

    frames = slice_by_indices(names, i1, i2)

    return ExpandedBoom(x, frames)
