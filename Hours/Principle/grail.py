# Grail
# Hunger - A craving, material or otherwise
# Indulge - Enjoying a passion


from Conveying.Wisdoms.grail import GrailWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Grail(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.GRAIL
        self.wisdom = GrailWisdom()
