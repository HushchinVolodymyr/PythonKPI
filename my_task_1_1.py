import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number1", type=float)
parser.add_argument("operator", type=str)
parser.add_argument("number2", type=float)

args = parser.parse_args()

if args.operator in ("+", "-", "*", "/"):
    print(args)
    print(eval(str(args.number1) + args.operator + str(args.number2)))
else:
    print("Not math symbol")
