# Winter
# Complete - Finish what is ending
# Awake - Revive that which is not quite dead


from Conveying.Wisdoms.winter import WinterWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Winter(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.WINTER
        self.wisdom = WinterWisdom()
