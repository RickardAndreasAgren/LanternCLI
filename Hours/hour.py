
from enum import unique, Enum, Flag, auto

from Hours.principletype import PrincipleInterface

@unique
class HourOptions(Flag):
    HEART = auto()
    GRAIL = auto()
    EDGE = auto()
    FORGE = auto()
    KNOCK = auto()
    LANTERN = auto()
    WINTER = auto()
    MOTH = auto()


class Hour(Enum):
    HEART = "heart" #0
    GRAIL = "grail" #1
    EDGE = "edge" #2
    FORGE = "forge" #3
    KNOCK = "knock" #4
    LANTERN = "lantern" #5
    WINTER = "winter" #6
    MOTH = "moth" #7
    
    def perindex(index:int) -> Enum:
        return list(Hour)[index]
    
    def getnear(self) -> list[Enum]:
        plus = 1 + self.hasindex()
        negative = self.hasindex() - 1
        if plus == 8:
            plus = 0
        if negative == -1:
            negative = 7
        return [Hour.perindex(negative),Hour.perindex(plus)]
    
    def getwithnear(self) -> list[Enum]:
        near = self.getnear()
        near.insert(1, self)
        return near
        
    def hasindex(self) -> int:
        hourlist = list(Hour)
        return hourlist.index(self)
    
    def getprinciple(self) -> PrincipleInterface:
        index = self.hasindex()
        