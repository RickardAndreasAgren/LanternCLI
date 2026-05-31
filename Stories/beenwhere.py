


from Space.places import SpaceInterface


class BeenInterface:
    
    @classmethod
    def remember(self, past:str):
        self.parsepast(past)
        return None
      
    def parsepast(self, past:str):
        return
      
    
class Beenwhere:
    def __init__(self):
      self.been = list(BeenInterface)
      return
       # store all locations their progress
       #
       
    def addlocation(self, been:BeenInterface):
        self.been.append(been)
        
    def getpast(self, been:SpaceInterface):
        #
        #
        # TODO
        return self.been[0]