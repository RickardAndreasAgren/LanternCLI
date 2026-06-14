# Moth
# Yearn - Long for something to come
# Unravel - Expose the unexpected


from Conveying.Wisdoms.moth import MothWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Moth(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.MOTH
        self.wisdom = MothWisdom()
