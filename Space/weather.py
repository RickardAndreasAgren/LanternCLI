
from enum import Enum, unique
import random
import time

from Light.above import Vector

# What the wind brought
#
#

# Clear
#
#

# Pockets
#
#

# Cloudy
#
#

# Trickle
#
#

# Rain
#
#

# Snow
#
#


class Season(Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


@unique
class Weather(Enum):
    CLEAR = "clear"
    POCKETS = "pockets"
    CLOUDY = "cloudy"
    TRICKLE = "trickle"
    RAIN = "rain"
    SNOW = "snow"

    
    @classmethod
    def stillweather(cls, season: Season, seed: int):
        
        return Weather.CLEAR

    @classmethod
    def breezeweather(cls, season: Season, seed: int):
        
        return Weather.CLEAR
    
    @classmethod
    def gustsweather(cls, season: Season, seed: int):
        
        return Weather.CLEAR
    
    @classmethod
    def windyweather(cls, season: Season, seed: int):
        
        return Weather.CLEAR
    
    @classmethod
    def stormyweather(cls, season: Season, seed: int):
        
        return Weather.CLEAR

    @classmethod
    def from_vector(cls, wind: Vector):
        random.seed("strengthofabove", 2)
        seeded = random.randint(1, 6)
        season = Weather.getseason()

        if wind == cls.STILL:
            return Weather.stillweather(season, seeded)
        if wind == cls.REEZE:
            return breezeweather(season, seeded)
        if wind == cls.GUSTS:
            return gustsweather(season, seeded)
        if wind == cls.WINDY:
            return windyweather(season, seeded)
        if wind == cls.STORMY:
            return stormyweather(season, seeded)

    @classmethod
    def getseason() -> Season:
        month = time.localtime().tm_mon
        if month < 6 and month > 2:
            return Season.SPRING
        if month < 9:
            return Season.SUMMER
        if month < 12:
            return Season.AUTUMN
        return Season.WINTER

    """ Weather modifiers by season
     0 CLEAR, 1 POCKETS, 2 CLOUDY, 3 TRICKLE, 4 RAIN, 5 SNOW
    """

    @classmethod
    def seasonweights(season: Season) -> list:
        if season == Season.SPRING:
            return [3, 2, 1, 0, 2, 2]
        if season == Season.SUMMER:
            return [4, 1, 1, 2, 2, 0]
        if season == Season.AUTUMN:
            return [1, 1, 2, 2, 3, 1]
        return [2, 1, 2, 1, 0, 4]
