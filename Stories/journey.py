# The journey so far
#
# Hours = progress of the hours
# Locations = location state
# Times = travels today
# Today = principles through the day
#


from Hours.hour import Hour
from Light.above import TimeOfDay
from Space.places import SpaceInterface
from Stories.beenwhere import BeenInterface, Beenwhere


class Journey:
    def __init__(self, *, experience:list[str]):
        self.loaded = experience
        self.Hours = []
        self.Locations = Beenwhere()
        self.Times = 0
        self.Today = []
        
    # set all starting values
    def provision(self):
        self.Hours = [0,0,0,0,0,0,0,0]
        self.Locations = Beenwhere()
        self.Today = [0,0,0,0,0,0,0,0]
        
    #load
    def sofar(self) -> bool:
        self.provision()
        self.hstr()
        self.lstr()
        self.tstr()
        self.dstr()
        return True
    
    # get the day
    def getgaps(self) -> int:
        return self.Times
    
    # not to soon
    def issoon(self) -> bool:
        now = TimeOfDay.now()
        currenttime = 1 + now.hasindex()
        return currenttime > self.Times
    
    # get all hours
    def gethours(self):
        return self.Hours
    
    # get a history
    def getpast(self, history:SpaceInterface):
        return self.Locations.getpast(history)
    
    # get the moods tapped
    def tapped(self) -> list[Hour]:
        # loop Today
        # find any of 2
        # translate into Hours
        pass
    
    #UPPDATERS
    
    # add hour counter
    def addhour(self, hour:Hour):
        self.Hours[hour.hasindex()] =+ 1
    
    # add location found
    def addfound(self, been:BeenInterface):
        self.Locations.addlocation(been)
        
    # add time
    def settime(self):
        now = TimeOfDay.now()
        self.Times = 1 + now.hasindex()
        
    # add dayprinciple
    def addtoday(self, hour:Hour):
        self.Today[hour.hasindex()] += 1
       
    # when now becomes then 
    def notnow(self) -> list[str]:
        before = list[str]()
        before.append(self.hlst())
        before.append(self.llst())
        before.append(self.tlst())
        before.append(self.dlst())
        return before
        
    #MEMORY
    #recall hours
    def hstr(self):
        pass
    
    #recall locations
    def lstr(self):
        pass
    
    #recall times
    def tstr(self):
        pass
    
    #recall dayprinciples
    def dstr(self):
        pass
    
    
    #PASSED
    #settle hours
    def hlst(self):
        pass
    
    #settle locations
    def llst(self):
        pass
    
    #settle times
    def tlst(self):
        pass
    
    def dlst(self):
        pass
