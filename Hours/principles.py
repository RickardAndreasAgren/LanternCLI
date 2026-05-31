
from enum import Enum, unique

from Hours.hour import Hour
from Hours.mood import Mood
from Light.above import TimeOfDay

# Her intent
#
#

# Heart
# Preserve - Ensure something endures
# Rest - Gather strength and continue

# Grail
# Hunger - A craving, material or otherwise
# Indulge - Enjoying a passion

# Edge
# Struggle - Meeting resistance
# Contradiction - Understanding a thought collision

# Forge
# Transform - Change shape and purpose
# Renew - End something to create something

# Knock
# Open - Enable a threshold
# Search - Find the hidden

# Lantern
# Illuminate - Make something under the light above the house visible
# Discover - Unmask the unknown

# Winter
# Complete - Finish what is ending
# Awaken - Revive that which is not quite dead

# Moth
# Yearn - Long for something to come
# Unravel - Expose the unexpected

# Option: Mood + Time = Principle


class PrincipleInterface:

    @classmethod
    def destinations() -> list[str]:
        return []

class Seek:
    def __init__(self, *, when: TimeOfDay, hour:Hour = None, mood:Mood = None):
        self.when = when
        self.hour = None
        self.mood = None
        
        if hour is not None:
            self.hour = hour
        if self.hour is None and mood is not None:
            self.mood = mood
    
    def checkmood(self) -> bool:
        if self.mood is None:
            return False
        return True
    
    def checkhour(self) -> bool:
        if self.hour is None:
            return False
        return True
    
    def ensurehour(self):
        if self.checkhour() is False:
            if self.checkmood() is False:
                self.hourfromwhen()
            else:
                self.hourfrommood()
                
    def hourfromwhen(self):
        if self.hour is None:
            indextime = self.when.now()
            # when = TimeOfDay
            # 
        
    
    def hourfrommood(self):
        indexmood = Mood.perindex(self.mood)
        
