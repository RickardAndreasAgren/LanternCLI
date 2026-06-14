# Heart
# Preserve - Ensure something endures
# Rest - Gather strength and continue


from Conveying.Wisdoms.heart import HeartWisdom
from Hours.hour import Hour
from ..principletype import PrincipleInterface

class Heart(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.HEART
        self.wisdom = HeartWisdom()
