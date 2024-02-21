import argparse
import cowsay


parser = argparse.ArgumentParser()
args = parser.parse_args()
print(cowsay.cowsay("Hello world!"))
