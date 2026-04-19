
# Run with options
#
# TODO adapt
def _build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for Lantern.

    Returns:
        A configured ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog="lantern",
        description=(
            "Bring a tool and use it somewhere, some time"
        ),
    )
    parser.add_argument(
        "--mood",
        type=str,
        default=None,
        choices=[m.value for m in Mood],
        help="emotional weather of the poem (default: random)",
    )
    parser.add_argument(
        "--hour",
        type=int,
        default=None,
        metavar="0–23",
        help="override the hour for time-of-day awareness (default: now)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="integer seed for reproducible output",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="show poem metadata (mood, time, arc, quality)",
    )
    return parser