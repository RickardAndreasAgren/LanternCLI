
from enum import Enum, unique
import random
import time

from Light.above import TimeOfDay, Vector

# What the wind brought
#
# Clear Pockets Cloudy Trickle Rain Snow


@unique
class Season(Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


@unique
class Clouds(Enum):
    CLEAR = "clear"
    POCKETS = "pockets"
    CLOUDY = "cloudy"
    TRICKLE = "trickle"
    RAIN = "rain"
    SNOW = "snow"
    
    def perindex(index:int) -> Enum:
        return list(Clouds)[index]
        


class Weather():
    def __init__(self, *, season: Season = None, vector: Vector = None):
        self.clouds = None
        self.season = None
        self.seed = None
        self.vector = Vector.NAV
        if season is not None:
            self.season = season
        if vector is not None:
            self.vector = vector

    def from_seasonandorvector(cls, *, space: Season = None,
                               vector: Vector = None):
        cls.seed = random.Random()
        cls.seed.seed("strengthfromabove", 2)
        if cls.season is None:
            cls.season = Weather.getseason()
        season = cls.season
        print(season)
        if cls.vector is Vector.NAV:
            when = TimeOfDay.now()
            cls.vector = Vector.from_shadows(TimeOfDay.shadows(when))
            
        vector = cls.vector
        print(vector)
        weatherweights = Weather.weatherweights(season)
        vectorweights = Weather.vectorweights(vector)
        index = 0
        weights = []
        for w in weatherweights:
            if vectorweights[index] == 0:
                weatherweights[index] = 0
            if w == 0:
                vectorweights[index] = 0
            weights.append(weatherweights[index] + vectorweights[index])
            index += 1

        seeded = cls.seed.randint(0, 19)
        print(seeded)
        index = 0
        while seeded > 0:
            seeded -= weights[index]
            if seeded > 0 and index < len(weights) - 1:
                index += 1
            else:
                cls.clouds = Clouds.perindex(index)
        print(cls.clouds)

    @classmethod
    def getseason(cls) -> Season:
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
    def weatherweights(cls, season: Season) -> list:
        if season == Season.SPRING:
            return [3, 2, 1, 0, 2, 2]
        if season == Season.SUMMER:
            return [4, 1, 1, 2, 2, 0]
        if season == Season.AUTUMN:
            return [1, 1, 2, 2, 3, 1]
        return [2, 1, 2, 1, 0, 4]

    """ Weather modifiers by vector
     0 CLEAR, 1 POCKETS, 2 CLOUDY, 3 TRICKLE, 4 RAIN, 5 SNOW
    """
    @classmethod
    def vectorweights(cls, wind: Vector) -> list:
        if wind == Vector.STILL:
            return [3, 2, 1, 2, 0, 2]
        if wind == Vector.BREEZE:
            return [1, 3, 1, 2, 2, 1]
        if wind == Vector.GUSTS:
            return [1, 2, 2, 1, 2, 2]
        if wind == Vector.WINDY:
            return [1, 0, 1, 1, 4, 3]
        if wind == Vector.STORMY:
            return [0, 1, 1, 0, 5, 3]