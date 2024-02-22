import argparse
import cowsay


parser = argparse.ArgumentParser()
# Parsing presets
presets = parser.add_argument_group("presets").add_mutually_exclusive_group()
presets.add_argument("-b", action="store_true", help="Borg")
for p in "dead", "greedy", "paranoid", "stoned", "tired", "wired", "youthful":
    presets.add_argument(f"-{p[0]}", action="store_true", help=p)
# Parsing eyes
parser.add_argument("-e", default="oo",
                    help="specify eyes appearance", metavar="eyes")
# Parsing tongue
parser.add_argument("-T", default='',
                    help="specify tongue appearance", metavar="tongue")

args = parser.parse_args()
preset = ''.join(p for p in "bdgpstwy" if getattr(args, p))

print(cowsay.cowsay(
    "Hello world!",
    preset=preset,
    eyes=args.e,
    tongue=args.T
))
