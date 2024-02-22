import argparse
import cowsay


parser = argparse.ArgumentParser()
# Parsing presets
presets = parser.add_argument_group("presets").add_mutually_exclusive_group()
presets.add_argument("-b", action="store_true", help="Borg")
for p in "dead", "greedy", "paranoid", "stoned", "tired", "wired", "youthful":
    presets.add_argument(f"-{p[0]}", action="store_true", help=p)

args = parser.parse_args()
preset = ''.join(p for p in "bdgpstwy" if getattr(args, p))

print(cowsay.cowsay(
    "Hello world!",
    preset=preset
))
