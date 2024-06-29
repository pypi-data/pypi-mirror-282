from boom2zoom.animation import BoomSwitch
from boom2zoom.settings import BOOM_DEFAULT_SWITCHES_PATH
from boom2zoom.utils import load_csv

BOOM_DEFAULT_SWITCHES = frozenset(
    BoomSwitch(
        off=row["off"],
        on=row["on"],
        type=int(row["type"]),
    )
    for row in load_csv(BOOM_DEFAULT_SWITCHES_PATH)
)
