


from typing import Final, List

from Conveying.wisdom import Jot, Ordered
from Hours.hour import HourOptions

t=Ordered.ABSTRACTION

Abstractions: Final[List[Jot]] = List[Jot](
    Jot("persistence", t, HourOptions.EDGE),
    Jot("contradiction", t, HourOptions.EDGE),
    
    Jot("renewal", t, HourOptions.EDGE|HourOptions.FORGE),
    
    Jot("becoming", t, HourOptions.FORGE),
    Jot("arriving", t, HourOptions.FORGE),
    
    Jot("gratification", t, HourOptions.FORGE|HourOptions.GRAIL),
    
    Jot("indulgence", t, HourOptions.GRAIL),
    Jot("yearning", t, HourOptions.GRAIL),
    
    Jot("tenderness", t, HourOptions.GRAIL|HourOptions.HEART),
    
    Jot("comfort", t, HourOptions.HEART),
    Jot("belonging", t, HourOptions.HEART),
    
    Jot("invitation", t, HourOptions.HEART|HourOptions.KNOCK),
    
    Jot("crossing", t, HourOptions.KNOCK),
    Jot("entrance", t, HourOptions.KNOCK),
    
    Jot("beginning", t, HourOptions.KNOCK|HourOptions.LANTERN),
    
    Jot("illumination", t, HourOptions.LANTERN),
    Jot("notion", t, HourOptions.LANTERN),
    
    Jot("fascination", t, HourOptions.LANTERN|HourOptions.MOTH),
            
    Jot("distance", t, HourOptions.MOTH),
    Jot("longing", t, HourOptions.MOTH),
    
    Jot("solitude", t, HourOptions.MOTH|HourOptions.WINTER),
    
    Jot("silence", t, HourOptions.WINTER),
    Jot("stillness", t, HourOptions.WINTER),
    
    Jot("ending", t, HourOptions.WINTER|HourOptions.EDGE),
)