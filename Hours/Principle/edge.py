# Edge
# Struggle - Meeting resistance
# Win - Finding victory after battle

from Hours.hour import Hour
from Conveying.Wisdoms.edge import EdgeWisdom
from ..principletype import PrincipleInterface

class Edge(PrincipleInterface):
    def __init__(self):
        self.hour = Hour.EDGE
        self.wisdom = EdgeWisdom()
