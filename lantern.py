
# What happens?
#
#


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for Lantern.

    A dynamic tool for the secret house.

    Args:
        argv: Command-line arguments. Uses sys.argv[1:] when None.
    """
    parser = _build_parser()
    args = parser.parse_args(argv)

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
        time_of_day = TimeOfDay.from_hour(datetime.now().hour)

    config = PoemConfig(
        mood=mood,
        time_of_day=time_of_day,
        line_count=args.lines,
        seed=args.seed,
    )