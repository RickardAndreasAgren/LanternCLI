
# Her mood
#
#

# Principle of the mood
# Option: Mood + Time = Principle
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
    BLUE = "blue"
