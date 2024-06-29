from __future__ import annotations

from collections import ChainMap, OrderedDict as ODict
from collections.abc import Mapping
from functools import reduce, cache
from itertools import chain

from PIL.Image import Image, alpha_composite, new as new_image
from omg import Graphic, WAD, Flat
from omg.txdef import TextureDef, Textures

from boom2zoom.settings import DATA_DIR
from boom2zoom.utils import hash_image_xxh3


class MissingPatchError(Exception):
    def __init__(self, patch: str, txdef: TextureDef):
        self.patch = patch
        self.txdef = txdef

    def __str__(self):
        return f"Missing patch {self.patch} for texture {self.txdef.name}"


@cache
def _load_texture_digests() -> set[int]:
    data_path = DATA_DIR / "texture_digests.txt"
    digests = set()
    with open(data_path) as f:
        for line in f:
            digests.add(int(line))
    return digests


def image_is_stock_texture(img: Image):
    """Check if a given image infringes on known stock textures.

    Args:
        img: The image to be checked.

    Returns:
        True if the image matches a known stock asset, False otherwise.

    """
    digests = _load_texture_digests()
    return hash_image_xxh3(img) in digests


def get_missing_patches(txdef: TextureDef, patches: Mapping[str, Graphic]) -> set[str]:
    """Returns a set of patch names that are present in *txdef* but missing from a *patches* mapping."""
    return set(patch.name for patch in txdef.patches) - set(patches)


def check_have_patches(txdef: TextureDef, patches: Mapping[str, Graphic]) -> bool:
    """Return True if all patches in *txdef* are found in *patches* mapping."""
    return all(patchdef.name in patches for patchdef in txdef.patches)


def render_texture(texture: TextureDef, patches: Mapping[str, Graphic]) -> Image:
    """Converts a texture to a Pillow Image.

    Args:
        texture: The texture definition to render.
        patches: Graphics to use for patch references

    Returns:
        Image: The rendered image

    Raises:
        MissingPatchError: If a patch is not available in the given *patches*.

    """
    # Image.paste alone is not suitable and does not respect transparency.
    # We construct the layers as separate images with the patch in the right place and then use
    # alpha_composite to flatten them.
    # REF: https://github.com/python-pillow/Pillow/issues/6142
    layers = []

    for patch_def in texture.patches:
        try:
            layer = new_image("RGBA", (texture.width, texture.height))
            pimg = patches[patch_def.name].to_Image("RGBA")
            layer.paste(pimg, (patch_def.x, patch_def.y))
            layers.append(layer)

        except KeyError as e:
            raise MissingPatchError(patch_def.name, texture) from e

    final_image = reduce(alpha_composite, layers)

    return final_image


def make_patch_lookup(*wads: WAD) -> ChainMap[str, Graphic]:
    """Merges sources of graphics from many wads into one mapping.

    Sources taken are the `wad.patches`, `wad.sprites`, `wad.graphics` maps. We also attempt to convert lumps in `.data`
    to `omg.Graphic` as a last resort and merge successful conversions.

    And the returned mapping looks up graphics in the same order: patches, then sprites, graphics, and finally, data.
    """

    # Since graphics may end up in data (like our own wad.wad test file), we try as a last resort
    # to see if any of its lumps are actually Doom graphics.
    converted_data = {}
    for wad in wads:
        for name, lump in wad.data.items():
            # noinspection PyBroadException
            try:
                graphic = Graphic(lump)
                graphic.to_Image(mode="RGBA")
            except Exception:  # pylint: disable=broad-except
                continue
            else:
                converted_data[name] = graphic

    graphic_sources = ((wad.patches, wad.sprites, wad.graphics) for wad in wads)
    sources = chain.from_iterable(graphic_sources)

    return ChainMap(*sources, converted_data)


def get_textures(wad: WAD) -> ODict[str, TextureDef]:
    return ODict(Textures(wad.txdefs).items())


def get_flats(wad: WAD) -> ODict[str, Flat]:
    return ODict(wad.flats.items())  # copy is broken in omg's OD subclasses
