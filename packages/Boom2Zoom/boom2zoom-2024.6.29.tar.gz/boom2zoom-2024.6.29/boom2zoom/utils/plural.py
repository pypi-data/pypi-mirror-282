"""Helpers to format plurals."""

PLURALS = {"texture": "textures", "flat": "flats", "definition": "definitions"}


def p(singular: str, count: int) -> str:
    """Return the plural form of a given singular noun based on the count.

    Parameters:
        singular: The singular form of the noun.
        count: The count of the items.

    Returns:
        str: The appropriate singular or plural form of the noun.

    Raises:
        ValueError: If the given word is not known.
    """
    if count == 1:
        return singular
    if singular in PLURALS:
        return PLURALS[singular]
    else:
        raise ValueError(f"Singular word '{singular}' is not known.")
