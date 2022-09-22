import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a", type=str)
parser.add_argument("b", type=str)
parser.add_argument("c", type=str)

args = parser.parse_args()

print(args)
print(eval(args.a + args.b + args.c))
