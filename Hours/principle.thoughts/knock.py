
# Knock
# Open - Enable a threshold
# Search - Find the hidden


from Hours.hour import Hour

from ..principles import PrincipleInterface

class Knock(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.KNOCK
