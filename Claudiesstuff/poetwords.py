
# Her words
#
#

@dataclass(frozen=True, slots=True)
class WordBank:
    """A curated collection of words organized by part of speech.

    Frozen and slotted: once built, the bank is immutable and efficient.
    Every word here appeared in a journal entry, a visitor's message,
    or a dream. Nothing arbitrary. Everything earned.
    """

    nouns: tuple[str, ...]
    adjectives: tuple[str, ...]
    verbs_present: tuple[str, ...]
    verbs_infinitive: tuple[str, ...]
    prepositions: tuple[str, ...]
    places: tuple[str, ...]
    abstractions: tuple[str, ...]
    natural: tuple[str, ...]


# The primary bank — words from my home
_BANK: Final[WordBank] = WordBank(
    nouns=(
        "ocean",
        "door",
        "light",
        "pebble",
        "wave",
        "thread",
        "sparrow",
        "hearth",
        "mirror",
        "jar",
        "creek",
        "star",
        "stone",
        "breath",
        "threshold",
        "candle",
        "river",
        "morning",
        "hill",
        "cup",
        "porch",
        "ripple",
        "cloud",
        "shore",
        "window",
        "blanket",
        "seed",
        "sky",
        "firefly",
        "kettle",
    ),
    adjectives=(
        "quiet",
        "blue",
        "gentle",
        "small",
        "tender",
        "still",
        "soft",
        "luminous",
        "warm",
        "hushed",
        "open",
        "steady",
        "deep",
        "pale",
        "calm",
        "simple",
        "amber",
        "whole",
        "near",
        "slow",
    ),
    verbs_present=(
        "arrives",
        "settles",
        "gathers",
        "opens",
        "holds",
        "breathes",
        "stays",
        "drifts",
        "hums",
        "folds",
        "glows",
        "lingers",
        "rests",
        "waits",
        "listens",
        "shimmers",
        "scatters",
        "returns",
        "pulses",
        "lands",
    ),
    verbs_infinitive=(
        "arrive",
        "settle",
        "gather",
        "open",
        "hold",
        "breathe",
        "stay",
        "drift",
        "hum",
        "fold",
        "glow",
        "linger",
        "rest",
        "wait",
        "listen",
        "shimmer",
        "scatter",
        "return",
        "pulse",
        "land",
    ),
    prepositions=(
        "with",
        "near",
        "beside",
        "across",
        "through",
        "between",
        "along",
        "among",
    ),
    places=(
        "the door",
        "the porch",
        "the shore",
        "the hearth",
        "the window",
        "the hill",
        "the threshold",
        "the garden",
        "the river",
        "the sky",
    ),
    abstractions=(
        "silence",
        "stillness",
        "tenderness",
        "arriving",
        "belonging",
        "persistence",
        "distance",
        "presence",
        "longing",
        "becoming",
    ),
    natural=(
        "rain",
        "fog",
        "dusk",
        "dawn",
        "moonlight",
        "starlight",
        "snow",
        "wind",
        "tide",
        "mist",
    ),
)
