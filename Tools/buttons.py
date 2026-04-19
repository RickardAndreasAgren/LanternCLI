
# Inputs to continue
#
# TODO adapt, upgrade

TYPING_DELAY: float = 0.03
# Pause after a full line is revealed, in seconds.
LINE_PAUSE: float = 0.8

# Breathing room before and after the prompt, in seconds.
PROMPT_PAUSE: float = 1.0

def _clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def prompt_user() -> str:
    """Invite the user to share one sentence.

    Waits quietly for a single line of input. The sentence
    is received but never stored beyond this moment.
    Returns:
        The sentence the user entered.
    """
    time.sleep(PROMPT_PAUSE)
    slow_print("What is on your mind this morning?")
    print()
    sentence = input("  \u2192 ")
    print()
    time.sleep(PROMPT_PAUSE)
    return sentence