# NOTES:

# Boom ANIMATED and SWITCHES lumps contain stock animation definitions. These end up in ANIMDEFS when Slade makes
# one (2024-03). They are not needed.

# In ANIMDEFS, the optional keyword does not always help; consider this error from ZDoom over a stock texture:
# Script error, "WAT.pk3:animdefs.txt" line 181:
# Unknown texture COMP04
# COMP04 is from a Strife animation.

__all__ = ["STOCK_ANIMATED"]

from boom2zoom.animation import BoomAnimation
from boom2zoom.animation.boom import AnimatedType

# We list the stock animation data here. In addition to the stock animations that end up in ANIMATED, some wads also
# include definitions for other games!

DOOM = [
    # flats
    {"type": 0, "first": "NUKAGE1", "last": "NUKAGE3", "tics": 8},
    {"type": 0, "first": "FWATER1", "last": "FWATER4", "tics": 8},
    {"type": 0, "first": "SWATER1", "last": "SWATER4", "tics": 8},
    {"type": 0, "first": "LAVA1", "last": "LAVA4", "tics": 8},
    {"type": 0, "first": "BLOOD1", "last": "BLOOD3", "tics": 8},
    {"type": 0, "first": "SLIME01", "last": "SLIME04", "tics": 8},
    {"type": 0, "first": "SLIME05", "last": "SLIME08", "tics": 8},
    {"type": 0, "first": "SLIME09", "last": "SLIME12", "tics": 8},
    {"type": 0, "first": "RROCK05", "last": "RROCK08", "tics": 8},
    # textures
    {"type": 1, "first": "FIREWALA", "last": "FIREWALL", "tics": 8},
    {"type": 1, "first": "FIRELAV3", "last": "FIRELAVA", "tics": 8},
    {"type": 1, "first": "FIREMAG1", "last": "FIREMAG3", "tics": 8},
    {"type": 1, "first": "FIREBLU1", "last": "FIREBLU2", "tics": 8},
    {"type": 1, "first": "BFALL1", "last": "BFALL4", "tics": 8},
    {"type": 1, "first": "SFALL1", "last": "SFALL4", "tics": 8},
    {"type": 1, "first": "WFALL1", "last": "WFALL4", "tics": 8},
    {"type": 1, "first": "DBRAIN1", "last": "DBRAIN4", "tics": 8},
    # allow decals
    {"type": 3, "first": "BLODGR1", "last": "BLODGR4", "tics": 8},
    {"type": 3, "first": "SLADRIP1", "last": "SLADRIP3", "tics": 8},
    {"type": 3, "first": "BLODRIP1", "last": "BLODRIP4", "tics": 8},
    {"type": 3, "first": "GSTFONT1", "last": "GSTFONT3", "tics": 8},
    {"type": 3, "first": "ROCKRED1", "last": "ROCKRED3", "tics": 8},
]

HERETIC = [
    # flats
    {"type": 0, "first": "FLTWAWA1", "last": "FLTWAWA3", "tics": 8},
    {"type": 0, "first": "FLTSLUD1", "last": "FLTSLUD3", "tics": 8},
    {"type": 0, "first": "FLTTELE1", "last": "FLTTELE4", "tics": 6},
    {"type": 0, "first": "FLTFLWW1", "last": "FLTFLWW3", "tics": 9},
    {"type": 0, "first": "FLTLAVA1", "last": "FLTLAVA4", "tics": 8},
    {"type": 0, "first": "FLATHUH1", "last": "FLATHUH4", "tics": 8},
    # textures
    {"type": 1, "first": "LAVAFL1", "last": "LAVAFL3", "tics": 6},
    {"type": 1, "first": "WATRWAL1", "last": "WATRWAL3", "tics": 4},
]

STRIFE = [
    # flats
    {"type": 0, "first": "F_CONVY1", "last": "F_CONVY2", "tics": 4},
    {"type": 0, "first": "F_FAN1", "last": "F_FAN2", "tics": 4},
    {"type": 0, "first": "F_HWATR1", "last": "F_HWATR3", "tics": 4},
    {"type": 0, "first": "F_PWATR1", "last": "F_PWATR3", "tics": 11},
    {"type": 0, "first": "F_RDALN1", "last": "F_RDALN4", "tics": 4},
    {"type": 0, "first": "F_SCANR1", "last": "F_SCANR4", "tics": 4},
    {"type": 0, "first": "F_SCANR5", "last": "F_SCANR8", "tics": 4},
    {"type": 0, "first": "F_TELE1", "last": "F_TELE2", "tics": 4},
    {"type": 0, "first": "P_VWATR1", "last": "F_VWATR3", "tics": 4},
    {"type": 0, "first": "F_WATR01", "last": "F_WATR03", "tics": 8},
    # textures
    {"type": 1, "first": "BRKGRY13", "last": "BRKGRY16", "tics": 10},
    {"type": 1, "first": "BRNSCN01", "last": "BRNSCN04", "tics": 10},
    {"type": 1, "first": "COMP01", "last": "COMP04", "tics": 4},
    {"type": 1, "first": "COMP05", "last": "COMP08", "tics": 6},
    {"type": 1, "first": "COMP09", "last": "COMP12", "tics": 11},
    {"type": 1, "first": "COMP13", "last": "COMP16", "tics": 12},
    {"type": 1, "first": "COMP17", "last": "COMP20", "tics": 12},
    {"type": 1, "first": "COMP21", "last": "COMP24", "tics": 12},
    {"type": 1, "first": "COMP25", "last": "COMP28", "tics": 12},
    {"type": 1, "first": "COMP29", "last": "COMP32", "tics": 12},
    {"type": 1, "first": "COMP33", "last": "COMP37", "tics": 12},
    {"type": 1, "first": "COMP38", "last": "COMP41", "tics": 12},
    {"type": 1, "first": "COMP42", "last": "COMP49", "tics": 10},
    {"type": 1, "first": "CONCRT09", "last": "CONCRT12", "tics": 11},
    {"type": 1, "first": "CONCRT22", "last": "CONCRT25", "tics": 11},
    {"type": 1, "first": "FAN01", "last": "FAN02", "tics": 4},
    {"type": 1, "first": "FORCE01", "last": "FORCE04", "tics": 4},
    {"type": 1, "first": "FORCE05", "last": "FORCE08", "tics": 4},
    {"type": 1, "first": "SCAN01", "last": "SCAN04", "tics": 4},
    {"type": 1, "first": "SCAN05", "last": "SCAN08", "tics": 4},
    {"type": 1, "first": "SWTRMG01", "last": "SWTRMG03", "tics": 4},
    {"type": 1, "first": "WALPMP01", "last": "WALPMP02", "tics": 16},
    {"type": 1, "first": "WALTEK16", "last": "WALTEK17", "tics": 8},
]

ALL = DOOM + HERETIC + STRIFE

STOCK_ANIMATED = frozenset(
    BoomAnimation(
        type=AnimatedType(row["type"]),
        first=str(row["first"]),
        last=str(row["last"]),
        tics=int(row["tics"]),
    )
    for row in ALL
)
"""Final set of all known stock animations."""
