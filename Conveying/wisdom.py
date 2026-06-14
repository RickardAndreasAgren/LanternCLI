# All words and how they can belong


from enum import Enum, Flag, unique
from typing import List

from Hours.hour import HourOptions
from Hours.principletype import PrincipleInterface

@unique
class Ordered(Enum):
    ABSTRACTION = "abstraction"
    ADJECTIVE = "adjective"
    NATURAL = "natural"
    NOUN = "noun"
    NOW = "now"
    PLACES = "places"
    PREPOSITION = "preposition"
    SOMETIME = "sometime"
    
#places 'sub-places' & synonyms
#natural from run state

class Jot:
    def __init__(self, jot:str, what:Ordered, forwith: HourOptions):
        self.jot = str
        self.what = what
        self.forwith = forwith
    
    def word(self):
        return self.jot
    
    def use(self, active: HourOptions):
        for key in list(self.forwith):
            if active.name == key:
                return True

class Glossary:
    def __init__(self, what:Ordered):
        self.type = what
        
    type: Ordered
    jots: List[Jot]
    
    def add(self, jot:Jot):
        self.jots.append(jot)
        
    def filterfrom(self, terms: List[Jot], forwith:HourOptions):
        for word in terms:
            if word.use(forwith):
                self.jots.append(word)

class WisdomInterface:
    def destinations(self) -> List[str]:
        return ["INTERFACE"]
        
#
# create Contemplate
# using principle, set up glossaries
# using active location, set up glossary
# using weather and shadows, set up glossary
#
#
class Contemplate:
    def __init__(self, hour: PrincipleInterface):
      self.principle = None

    def consider() -> str:
        return ''
    
    