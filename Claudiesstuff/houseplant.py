#!/usr/bin/env python3
"""A houseplant, because green is nice."""

import random

# ANSI colors
DARK_GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
TERRACOTTA = "\033[38;5;173m"
PINK = "\033[38;5;211m"
YELLOW = "\033[93m"
SOIL = "\033[38;5;95m"
RESET = "\033[0m"
DIM = "\033[2m"

GREENS = [DARK_GREEN, BRIGHT_GREEN, "\033[38;5;28m", "\033[38;5;34m", "\033[38;5;71m"]
FLOWER_COLORS = [PINK, YELLOW, "\033[38;5;216m", "\033[38;5;183m"]


def make_plant():
    W = 32
    lines = []
    mid = W // 2

    num_stems = random.randint(3, 5)
    stems = []

    for _ in range(num_stems):
        height = random.randint(4, 8)
        drift = 0
        stem = []
        for h in range(height):
            drift += random.choice([-1, 0, 0, 1])
            drift = max(-3, min(3, drift))
            has_left = random.random() < 0.45 and h > 0
            has_right = random.random() < 0.45 and h > 0
            stem.append((drift, has_left, has_right))
        stems.append(stem)

    max_h = max(len(s) for s in stems)

    # Render plant rows (top to bottom)
    plant_rows = []
    for row in range(max_h):
        chars = [' '] * W
        colors = [''] * W

        for si, stem in enumerate(stems):
            spread = (si - num_stems // 2) * 2
            h_from_bottom = max_h - 1 - row
            if h_from_bottom >= len(stem):
                continue
            drift, has_left, has_right = stem[h_from_bottom]
            col = mid + spread + drift

            if col < 1 or col >= W - 1:
                continue

            g = random.choice(GREENS)

            # Stem character
            chars[col] = random.choice(['│', '┃', '╽']) if h_from_bottom > 0 else '│'
            colors[col] = g

            # Top of stem: flower or leaf crown
            if h_from_bottom == len(stem) - 1:
                if random.random() < 0.35:
                    chars[col] = random.choice(['✿', '❀', '✾', '❁'])
                    colors[col] = random.choice(FLOWER_COLORS)
                else:
                    chars[col] = random.choice(['♠', '♣', '❦', '✦'])
                    colors[col] = BRIGHT_GREEN

            # Leaves along the stem
            if has_left and col > 1:
                chars[col - 1] = random.choice([')', '}', '>', '⌉', '❧'[0]])
                colors[col - 1] = random.choice(GREENS)
            if has_right and col < W - 2:
                chars[col + 1] = random.choice(['(', '{', '<', '⌈'])
                colors[col + 1] = random.choice(GREENS)

        rendered = ''
        for c, clr in zip(chars, colors):
            if c != ' ':
                rendered += clr + c + RESET
            else:
                rendered += c
        plant_rows.append(rendered)

    # --- Pot ---
    pot_w = 14
    pot_left = mid - pot_w // 2

    pot_lines = []

    # Soil rim
    soil = SOIL + '┌' + '─' * pot_w + '┐' + RESET
    pot_lines.append(' ' * (pot_left - 1) + soil)

    # Soil surface
    soil_fill = SOIL + '│' + DARK_GREEN + ''.join(
        random.choice(['·', '.', ',', ':', ' ']) for _ in range(pot_w)
    ) + SOIL + '│' + RESET
    pot_lines.append(' ' * (pot_left - 1) + soil_fill)

    # Pot body (tapered)
    for i in range(4):
        w = pot_w - (i * 2)
        if w < 4:
            break
        left = pot_left + i
        if i == 0:
            body = TERRACOTTA + '┃' + '▒' * w + '┃' + RESET
        else:
            body = TERRACOTTA + '┃' + '░' * w + '┃' + RESET
        pot_lines.append(' ' * left + body)

    # Base
    base_w = pot_w - 6
    if base_w < 2:
        base_w = 2
    base_left = pot_left + 4
    base = TERRACOTTA + '╰' + '─' * base_w + '╯' + RESET
    pot_lines.append(' ' * base_left + base)

    # Assemble
    lines.append('')
    lines.extend(plant_rows)
    lines.extend(pot_lines)
    lines.append('')

    # Label, centered loosely
    label = DIM + '       a plant, because green is nice' + RESET
    lines.append(label)
    lines.append('')

    return '\n'.join(lines)


if __name__ == '__main__':
    print(make_plant())