
# The angle of the light from beyond
#
#

# The length of the shadows
#
#

# Darkness
# 21, 0, 3
#

# Long
# 6, 18
#

# Short
# 9, 15
#

# Gone
# 12
#

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
    TENDER_HOURS = "tender_hours"

    @classmethod
    def from_hour(cls, hour: int) -> TimeOfDay:
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