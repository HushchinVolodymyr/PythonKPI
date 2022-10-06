mport argparse

parser = argparse.ArgumentParser()

parser.add_argument("number1", type=int)
parser.add_argument("operator", type=str)
parser.add_argument("number2", type=int)

args = parser.parse_args()

if args.number2 == 0 and args.operator in ("/"):
    print("Сannot be divided by zero")
elif args.operator in ("+", "-", "*", "/"):
    print(args)
    print(eval(str(args.number1) + args.operator + str(args.number2)))
else:
    print(" or Not math symbol")
