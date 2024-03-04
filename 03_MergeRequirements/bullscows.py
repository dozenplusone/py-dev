import random
import sys
import urllib.request


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


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    ctr = 1
    while (guess := ask("Введите слово: ", words)) != secret:
        inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
        ctr += 1
    inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
    return ctr


if len(sys.argv) < 2:
    print("Нет словаря!")
    sys.exit(1)

try:
    src = urllib.request.urlopen(sys.argv[1])
except Exception:
    src = open(sys.argv[1], "rb")

length = int(sys.argv[2]) if len(sys.argv) > 2 else 5
words = [s for s in src.read().decode().split() if len(s) == length]
src.close()
