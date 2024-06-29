from collections.abc import Mapping
from typing import TypeAlias

from omg import Graphic, Flat
from omg.txdef import TextureDef

# TODO: use builtin type to declare aliases when nuitka supports it
TextureDefs: TypeAlias = Mapping[str, TextureDef]
Graphics: TypeAlias = Mapping[str, Graphic]
Flats: TypeAlias = Mapping[str, Flat]
