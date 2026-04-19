"""
firefly.py — A small evening ritual.

Press Enter to release a firefly into the jar.
Watch the light gather. Stop when it feels enough.
Nothing is saved. Each run starts empty.
"""
import math
import os
import random
import select
import sys
import time

# --- jar geometry ---
W, H = 34, 14
LEFT, RIGHT, TOP, BOT = 4, 29, 2, 12

# --- soft words that surface sometimes ---
WORDS = [
    "stillness", "enough", "warmth", "gentle", "here",
    "quiet", "held", "rest", "light", "soft", "home",
]

CLOSINGS = [
    ("The jar is full of light.", "That's enough for tonight.", "Good night."),
    ("The lights have gathered.", "Nothing left to do.", "Sleep well."),
    ("Look at all that gentle light.", "You did that.", "Good night."),
    ("The jar holds enough.", "So do you.", "Rest now."),
]

# --- jar outlines (dim → medium → bright) ---
_STYLES = [(".", ":"), ("-", "|"), ("─", "│")]


def _make_jar(rim: str, wall: str) -> list[str]:
    """Build a jar template from rim and wall characters."""
    r = rim * 15
    inner = " " * 19
    rows = [f"          {r}"]
    rows.append(f"         {wall}{' ' * 15}{wall}")
    rows.append(f"        {wall}{' ' * 17}{wall}")
    for _ in range(9):
        rows.append(f"       {wall}{inner}{wall}")
    rows.append(f"        {wall}{' ' * 17}{wall}")
    rows.append(f"         {rim * 19}")
    return rows


JAR_TEMPLATES = [_make_jar(r, w) for r, w in _STYLES]


class Firefly:
    """A single small light."""

    __slots__ = ("x", "y", "phase", "speed", "dx")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.phase = random.uniform(0, 6.28)
        self.speed = random.uniform(0.4, 1.0)
        self.dx = random.uniform(-0.3, 0.3)

    def glyph(self) -> str:
        w = math.sin(self.phase)
        if w > 0.3:
            return random.choice(("✦", "✧", "*"))
        return "·" if w > -0.3 else " "

    def drift(self) -> None:
        self.y -= 0.05 * self.speed
        self.x += self.dx * 0.1 * math.sin(self.phase * 0.7)
        self.phase += 0.12 * self.speed
        # stay inside the jar
        if self.y < TOP + 1:
            self.y = TOP + 1.5
            self.speed *= 0.5
        self.x = max(LEFT + 1.0, min(RIGHT - 1.0, self.x))


def _out(s: str) -> None:
    sys.stdout.write(s); sys.stdout.flush()

def _clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _render(flies: list, word: str, n: int) -> None:
    """Draw the jar with fireflies."""
    glow = 0 if n < 4 else (1 if n < 10 else 2)
    template = JAR_TEMPLATES[glow]

    # start with template as mutable grid
    grid: list[list[str]] = [list(row.ljust(W + 10)) for row in template]

    # place fireflies
    for f in flies:
        fy, fx = int(round(f.y)), int(round(f.x))
        if 1 <= fy < H - 1 and 0 <= fx < len(grid[fy]):
            ch = f.glyph()
            if ch != " ":
                grid[fy][fx] = ch

    # ambient glow when jar is filling
    if n > 10:
        for y in range(TOP + 1, BOT):
            for x in range(LEFT + 1, RIGHT):
                if x < len(grid[y]) and grid[y][x] == " ":
                    if random.random() < 0.03:
                        grid[y][x] = "·"

    # compose
    _out("\033[H\n")
    for row in grid:
        _out("   " + "".join(row) + "\n")
    _out("\n" + (f"                {word}\n" if word else "\n"))
    prompt = "   Press Enter.\n" if n < 5 else "   Press Enter.   (or q to go)\n"
    _out("\n" + prompt + "\n")


def _opening() -> None:
    _clear()
    _out("\033[?25l")  # hide cursor
    lines = [
        "A jar.", "Night air.", "Small lights waiting.", "",
        "Press Enter to release a firefly.",
        "Go slowly. There is nothing to finish.",
    ]
    _out("\n\n")
    for line in lines:
        _out(f"   {line}\n")
        time.sleep(0.5)
    _out("\n")
    time.sleep(1.0)


def _closing() -> None:
    _clear()
    msg = random.choice(CLOSINGS)
    _out("\n\n")
    time.sleep(1.0)
    for line in msg:
        _out(f"   {line}\n\n")
        time.sleep(0.8)
    time.sleep(2.0)
    _out("\033[?25h")  # show cursor


def _input_ready() -> bool:
    if os.name == "nt":
        import msvcrt
        return bool(msvcrt.kbhit())
    return bool(select.select([sys.stdin], [], [], 0)[0])


def main() -> None:
    """The whole small ritual."""
    flies: list[Firefly] = []
    threshold = random.randint(15, 23)
    word, word_ttl = "", 0.0
    n = 0

    _opening()
    _clear()
    _render(flies, "", n)

    # enter cbreak mode for single-key input
    raw = False
    old = None
    try:
        import termios
        import tty
        old = termios.tcgetattr(sys.stdin)
        tty.cbreak(sys.stdin.fileno())
        raw = True
    except (ImportError, Exception):
        pass

    try:
        last = time.time()
        while True:
            now = time.time()

            # gentle drift
            if now - last > 0.15:
                for f in flies:
                    f.drift()
                last = now
                if word_ttl > 0:
                    word_ttl -= 0.15
                    if word_ttl <= 0:
                        word = ""
                _render(flies, word, n)

            # check input
            if _input_ready():
                if raw:
                    ch = sys.stdin.read(1)
                    if ch == "q":
                        break
                    if ch not in ("\n", "\r"):
                        continue
                else:
                    try:
                        line = sys.stdin.readline().strip()
                    except EOFError:
                        break
                    if line == "q":
                        break

                # release a firefly
                x = random.uniform(LEFT + 2, RIGHT - 2)
                y = random.uniform(BOT - 3, BOT - 1)
                flies.append(Firefly(x, y))
                n += 1

                time.sleep(random.uniform(0.1, 0.2))

                # soft word sometimes
                if n > 2 and random.random() < 0.35:
                    word = random.choice(WORDS)
                    word_ttl = 2.5

                # completion
                if n >= threshold:
                    _render(flies, "", n)
                    time.sleep(2.5)
                    break

                _render(flies, word, n)

            time.sleep(0.05)

    except KeyboardInterrupt:
        pass
    finally:
        if raw and old is not None:
            import termios
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
        _closing()


if __name__ == "__main__":
    main()