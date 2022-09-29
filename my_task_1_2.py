import argparse

parser = argparse.ArgumentParser()

parser.add_argument("operator", type=str)
parser.add_argument("number", type=float)
parser.add_argument("number", type=float)

args = parser.parse_args()


def add(a, b):
    return a + b


def min(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b



if args.operator == "add":
    print(add(args.first_number, args.second_number))
elif args.operator == "min":
    print(min(args.first_number, args.second_number))
elif args.operator == "mult":
    print(mult(args.first_number, args.second_number))
elif args.operator == "div":
    print(div(args.first_number, args.second_number))
else:
    print("Data eror")
