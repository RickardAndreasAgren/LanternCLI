
from enum import Enum, unique

from Hours.hour import Hour
from Hours.mood import Mood

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
# Win - Finding victory after battle

# Forge
# Transform - Change shape and purpose
# Renew - End something to create something

# Knock
# Open - Enable a threshold
# Search - Find the hidden

# Lantern
# Illuminate - Make the house visible
# Discover - Find something under the light above the house

# Winter
# Complete - Finish what is ending
# Awake - Revive that which is not quite dead

# Moth
# Yearn - Long for something to come
# Unravel - Expose the unexpected

# Option: Mood + Time = Principle


class PrincipleInterface:

    @classmethod
    def destinations() -> list[str]:
        return []

class Seek:
    def __init__(self, *, hour:Hour = None, mood:Mood = None):
        self.hour = None
        self.mood = None
        
        if hour is not None:
            self.hour = hour
        if self.hour is None and mood is not None:
            self.mood = mood
    
    def checkmood() -> bool:
        
        return True
    
    def checkhour() -> bool:
        
        return True
    
    # TODO how though?
    #def 