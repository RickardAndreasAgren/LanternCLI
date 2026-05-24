# Grail
# Hunger - A craving, material or otherwise
# Indulge - Enjoying a passion


from Hours.hour import Hour

from ..principles import PrincipleInterface

class Grail(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.GRAIL
