
# Where the lantern is
#
#

# Garden
# Where things can be planted
#

# Woods
#
# Explore?

# Edge
# Where things can be added
# JSON-exist & plugin

# Beyond
# A surprise
#

from Light.above import TimeOfDay

# common interface for all the spaces
class SpaceInterface:

    @classmethod
    def validtimeofday() -> list[TimeOfDay]:
        return []
      
class SpaceDestination(SpaceInterface):
  pass

class SpaceNearby(SpaceInterface):
  pass

class SpaceInside(SpaceInterface):
  pass


