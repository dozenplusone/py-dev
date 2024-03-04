def bullscows(guess: str, secret: str) -> tuple[int, int]:
    bulls, cows = [], []
    for i, c in enumerate(guess):
        if c == secret[i]:
            bulls.append(i)
        elif c in secret:
            cows.append(i)
    return len(bulls), len(cows)
