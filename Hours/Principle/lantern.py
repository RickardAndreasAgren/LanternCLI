# Lantern
# Illuminate - Make the house visible
# Discover - Find something under the light above the house


from Conveying.Wisdoms.lantern import LanternWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Lantern(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.LANTERN
        self.wisdom = LanternWisdom()
