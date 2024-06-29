"""Helpers to load and save data with CSV."""

from __future__ import annotations

import csv
from collections.abc import Iterable, Mapping, Iterator
from pathlib import Path
from typing import Any


def save_csv(data: Iterable[Mapping[Any, Any]], dest: Path | str) -> None:
    """Saves an iterable of mappings to a CSV formatted text file.

    The first object's keys will be used to determine the header row fields.

    Args:
        data: An iterable of objects to be saved.
        dest: A file path (Path or str)

    Raises:
        ValueError: If *data* is empty.
        TypeError: If an object from *data* is unsupported.
    """
    data = iter(data)
    first_row = next(data, None)

    if first_row is None:
        raise ValueError("The iterable of objects is empty.")

    fieldnames = first_row.keys()

    with open(dest, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(first_row)

        for obj in data:
            writer.writerow(obj)


def load_csv(source: Path) -> Iterator[dict[str, str]]:
    """Load a CSV file and yield each row as a dictionary."""
    with source.open(mode="r", newline="") as file:
        yield from csv.DictReader(file)
