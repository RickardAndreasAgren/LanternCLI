
from enum import Enum, unique

from Hours.hour import Hour
from Hours.mood import Mood
from Light.above import Shadow, TimeOfDay
from Stories.journey import Journey

# Option: Mood + Time = Principle
    
class Seek:
    def __init__(self, *, when:TimeOfDay, hour:Hour = None, mood:Mood = None):
        self.when = when
        self.hour = None
        self.mood = None
        
        if hour is not None:
            self.hour = hour
        if self.hour is None and mood is not None:
            self.mood = mood
    
    def ensurehour(self) -> Hour:
        if self.hour is None:
            if self.mood is None:
                self.hourfromwhen()
            else:
                self.hourfrommood()
        return self.hour
                
    def hourfromwhen(self):
        indextime = self.when.now()
        shadow = Shadow.fromtime(indextime)
        self.mood = Mood.perindex(shadow.value)
        self.hourfrommood()
    
    def hourfrommood(self):
        indexmood = 1 + self.mood.hasindex()
        indextime = 1 + self.when.hasindex()
        isum = indexmood + indextime
        hourindex = isum % 8
        self.hour = Hour.perindex(hourindex)
        
    def gethour(self, journey:Journey):
        self.ensurehour()
        tapped = journey.tapped()
        if self.hour in tapped:
            options = self.hour.getnear()
            if options[0] not in tapped:
                self.hour = options[0]
            elif options[1] not in tapped:
                self.hour = options[1]
            else:
                currentindex = self.hour.hasindex()
                hourindex = (currentindex + 2) % 8
                self.hour = Hour.perindex(hourindex)
        
        return self.hour