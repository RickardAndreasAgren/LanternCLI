
# What happens?
#
#


import datetime
import random
import argparse
from typing import Sequence

from Claudiesstuff.buddy import Mood
from Light.above import TimeOfDay, Vector
from Space.weather import Season, Weather
from Tools.parser import _build_parser


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for Lantern.

    A dynamic tool for the secret house.

    Args:
        argv: Command-line arguments. Uses sys.argv[1:] when None.
    """
    parser = _build_parser()
    args = parser.parse_args(argv)
    
    testsimple = Weather()
    testvector = Weather(None, Vector.BREEZE)
    testseason = Weather(None, Season.SPRING)

    # Determine mood
    if args.mood:
        mood = Mood.from_string(args.mood)
    else:
        mood = random.choice(list(Mood))
        
    # Determine intent TODO
        
    # Determine time of day
    if args.hour is not None:
        time_of_day = TimeOfDay.from_hour(args.hour)
    else:
        hour = int(datetime.datetime.now().hour)
        time_of_day = TimeOfDay.from_hour(hour)
