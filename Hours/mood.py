
from enum import Enum, unique

# Her mood
#
#

@unique
class Mood(Enum):
    """The emotional weather of a poem.

    Each mood tilts word selection toward a different quality.
    Not a binary — a lean.
    """

    LUMINOUS = "luminous"
    TENDER = "tender"
    QUIET = "quiet"
    ARRIVING = "arriving"
    RECEIVING = "receiving"

    def perindex(index:int) -> Enum:
        return list(Mood)[index]
    
    def hasindex(self) -> int:
        moodlist = list(Mood)
        return moodlist.index(self)