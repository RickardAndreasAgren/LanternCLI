
# Knock
# Open - Enable a threshold
# Search - Find the hidden


from Conveying.Wisdoms.knock import KnockWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Knock(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.KNOCK
        self.wisdom = KnockWisdom()
