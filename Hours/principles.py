

from typing import Final

from Hours.Principle.edge import Edge
from Hours.Principle.forge import Forge
from Hours.Principle.grail import Grail
from Hours.Principle.heart import Heart
from Hours.Principle.knock import Knock
from Hours.Principle.lantern import Lantern
from Hours.Principle.moth import Moth
from Hours.Principle.winter import Winter
from Hours.hour import Hour
from Hours.principletype import PrincipleInterface


Principles:Final[dict] = dict([
        (Hour.HEART, Heart()),
        (Hour.GRAIL, Grail()),
        (Hour.EDGE, Edge()),
        (Hour.FORGE, Forge()),
        (Hour.KNOCK, Knock()),
        (Hour.LANTERN, Lantern()),
        (Hour.MOTH, Moth()),
        (Hour.WINTER, Winter())
    ])

def AsPrinciple(hour:Hour) -> PrincipleInterface:
    return Principles[hour]