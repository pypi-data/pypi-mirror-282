from __future__ import annotations

import zlib

from PIL.Image import Image
from xxhash import xxh3_64_intdigest

from .collections import *
from .csv_utils import *
from .plural import *


def hash_image_xxh3(img: Image) -> int:
    """Returns the XXH3 digest of the given Pillow image."""
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    image_bytes = img.tobytes()  # pyright: ignore[reportUnknownMemberType]
    return xxh3_64_intdigest(image_bytes)


def save_image_to_png(img: Image, dest: Path | str, compress_level: int = 2) -> None:
    """Save a Pillow image to disk.

    The parent directory is created if it doesn't exist.

    Args:
        img: The Pillow image to save.
        dest: The file path to save the image to.
        compress_level: A number between 0 and 9, where 0 is no compression and 9 is most.
    """
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, compress_level=compress_level)


def calc_file_crc32(path: Path | str, chunk_size: int = 1024 * 64) -> int:
    """Calculate the CRC32 checksum for a file.

    The file will be read in chunks of *chunk_size*, which defaults to 64KiB.

    Returns:
        The CRC32 checksum of the file contents as an integer.
    """
    crc32 = 0
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            crc32 = zlib.crc32(chunk, crc32)
    return crc32
