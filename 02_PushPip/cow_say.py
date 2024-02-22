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
# Parsing cow file
parser.add_argument("-f", help="specify cow picture file (built-in or custom)",
                    metavar="cowfile")
# Showing cows list
parser.add_argument("-l", action="store_true",
                    help="show list of built-in cow files and exit")
# Parsing tongue
parser.add_argument("-T", default='',
                    help="specify tongue appearance", metavar="tongue")

args = parser.parse_args()
avail = sorted(cowsay.list_cows())
preset = ''.join(p for p in "bdgpstwy" if getattr(args, p))

if args.l:
    print("Built-in cow files:")
    print(*avail)
elif args.f is None:
    # cow file not specified
    print(cowsay.cowsay(
        "Hello world!",
        preset=preset,
        eyes=args.e,
        tongue=args.T
    ))
elif args.f in avail:
    # cow file is built-in
    print(cowsay.cowsay(
        "Hello world!",
        cow=args.f,
        preset=preset,
        eyes=args.e,
        tongue=args.T
    ))
else:
    # cow file is custom *.cow
    with open(args.f) as f:
        cowfile = cowsay.read_dot_cow(f)
    print(cowsay.cowsay(
        "Hello world!",
        preset=preset,
        eyes=args.e,
        tongue=args.T,
        cowfile=cowfile
    ))
