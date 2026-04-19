
# For files to read and write
#
# TODO: adapts

def _cmd_add(path: Path, text: str | None) -> int:
    """Adds a new pebble to the jar."""
    if text is None:
        try:
            text = input("  what's something good? ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 1

    if not text:
        _put("a pebble needs a few words.")
        return 1

    pebbles = _load(path)
    pebbles.append(_new_pebble(text))
    _save(path, pebbles)
    _put("noted.")
    return 0


def _cmd_shake(path: Path) -> int:
    """Randomly surfaces a handful of past pebbles."""
    pebbles = _load(path)

    if not pebbles:
        _put("your jar is empty.")
        _put('try: pebbles add "something good"')
        return 0

    count = min(len(pebbles), random.randint(_SHAKE_MIN, _SHAKE_MAX))
    chosen = random.sample(pebbles, count)

    _put()
    for pebble in chosen:
        _put(f"  \u00b7 {pebble.text}")
    _put()
    return 0


def _cmd_list(path: Path) -> int:
    """Lists all pebbles in chronological order."""
    pebbles = _load(path)

    if not pebbles:
        _put("no pebbles yet.")
        return 0

    _put()
    for pebble in pebbles:
        date = _format_date(pebble.timestamp)
        _put(f"{date}  {pebble.text}")
    _put()
    return 0


def _cmd_clear(path: Path) -> int:
    """Removes all pebbles after user confirmation."""
    pebbles = _load(path)

    if not pebbles:
        _put("already empty.")
        return 0

    count = len(pebbles)
    noun = _pluralize(count)

    try:
        answer = input(f"  remove {count} {noun}? [y/N] ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return 1

    if answer not in ("y", "yes"):
        _put("kept everything.")
        return 0

    _save(path, [])
    _put("jar emptied.")
    return 0