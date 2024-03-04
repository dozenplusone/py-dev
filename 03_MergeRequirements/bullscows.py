def bullscows(guess: str, secret: str) -> tuple[int, int]:
    bulls, cows = [], []
    for i, c in enumerate(guess):
        if c == secret[i]:
            bulls.append(i)
        elif c in secret:
            cows.append(i)
    return len(bulls), len(cows)


def ask(prompt: str, valid: list[str] = None) -> str:
    ans = input(prompt)
    if valid is not None:
        while ans not in valid:
            ans = input(prompt)
    return ans


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
