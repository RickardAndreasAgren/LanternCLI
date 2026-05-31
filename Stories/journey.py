# The journey so far
#
# Hours = progress of the hours
# Locations = location state
# Times = travels today
# Today = principles through the day
#


from Hours.hour import Hour
from Stories.beenwhere import Beenwhere


class Journey:
    def __init__(self, *, experience:list[str]):
        self.loaded = experience
        self.Hours = []
        self.Locations = Beenwhere
        self.Times = 0
        self.Today = []
    
    #
    def gethours(self):
        return self.Hours
    
    # add hour counter
    def addhour(self, hour:Hour):
        self.Hours[Hour.hasindex()] =+ 1
        

    def provision(self):
        self.Hours = [0,0,0,0,0,0,0,0]
        self.Locations = BeenWhere()
        
    #load
    def sofar(self):
        