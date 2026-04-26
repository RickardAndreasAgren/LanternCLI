
from enum import Enum, unique
import time
import random

# The angle of the light from beyond
# The length of the shadows
# The strength of air


class Shadow(Enum):
    HIDDEN = 0
    SHORT = 1
    REACHING = 2
    TOWERING = 3
    FULL = 4


@unique
class TimeOfDay(Enum):
    """The hour's character.
    """

    DAWN = "dawn"
    MORNING = "morning"
    DAY = "day"
    AFTERNOON = "afternoon"
    DUSK = "dusk"
    EVENING = "evening"
    NIGHT = "night"
    TENDER_HOURS = "tender hours"

    @classmethod
    def from_hour(cls, hour: int):
        """Determine the time of day from a 24-hour clock value.

        Args:
            hour: The hour (0-23).

        Returns:
            The corresponding TimeOfDay.
        """
        if hour < 0 or hour > 23:
            msg = f"Hour must be 0-23, got {hour}"
            raise ValueError(msg)
        if 2 <= hour <= 4:
            return cls.TENDER_HOURS
        if 5 <= hour <= 7:
            return cls.DAWN
        if 8 <= hour <= 10:
            return cls.MORNING
        if 11 <= hour <= 13:
            return cls.DAY
        if 14 <= hour <= 16:
            return cls.AFTERNOON
        if 17 <= hour <= 19:
            return cls.DUSK
        if 20 <= hour <= 22:
            return cls.EVENING
        return cls.NIGHT  # 23, 0, 1

    @classmethod
    def shadows(cls, TimeOfDay):
        """
            Reach of darkness
        """
        if TimeOfDay == cls.NIGHT:
            return Shadow.FULL
        if TimeOfDay == cls.TENDER_HOURS or TimeOfDay == cls.EVENING:
            return Shadow.TOWERING
        if TimeOfDay == cls.DAWN or TimeOfDay == cls.DAWN:
            return Shadow.REACHING
        if TimeOfDay == cls.MORNING or TimeOfDay == cls.AFTERNOON:
            return Shadow.SHORT
        if TimeOfDay == cls.DAY:
            return Shadow.HIDDEN

    @classmethod
    def now(cls):
        hour = time.localtime().tm_hour
        return TimeOfDay.from_hour(hour)


@unique
class Vector(Enum):
    """Weather strength
    """

    NAV = "notavector"
    STILL = "calm"
    BREEZE = "breezing"
    GUSTS = "gusting"
    WINDY = "windy"
    STORMY = "stormy"

    @classmethod
    def from_shadows(cls, darkness: Shadow):
        random.seed("shadowsofthewind", 2)
        seeded = random.randint(1, 5)
        if darkness == Shadow.FULL:
            if seeded > 3:
                return Vector.STORMY
            if seeded > 2:
                return Vector.WINDY
            return Vector.STILL
        if darkness == Shadow.TOWERING:
            if seeded > 4:
                return Vector.STORMY
            if seeded > 3:
                return Vector.GUSTS
            return Vector.BREEZE
        if darkness == Shadow.REACHING:
            if seeded > 4:
                return Vector.WINDY
            if seeded > 3:
                return Vector.BREEZE
            return Vector.STILL
        if darkness == Shadow.SHORT:
            if seeded > 4:
                return Vector.WINDY
            if seeded > 2:
                return Vector.GUSTS
            return Vector.BREEZE
        if darkness == Shadow.HIDDEN:
            if seeded > 4:
                return Vector.STORMY
            if seeded > 2:
                return Vector.WINDY
            return Vector.STILL
