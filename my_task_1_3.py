import argparse

parser = argparse.ArgumentParser()

parser.add_argument("expressions", type=str)

args = parser.parse_args()

char_list = list(args.expressions)

print(char_list)


def empty_line(list1, str_exp):
    return list1[0].isdigit() and list1[-1].isdigit and "++" not in str_exp and "--" not in str_exp


def calc(list1, str_exp):
    try:
        if empty_line(list1, str_exp):
            print("True,", eval(args.expressions))
        else:
            print("False, None")
    except (IndexError, TypeError, KeyError, SyntaxError, NameError, KeyboardInterrupt, EOFError):
        print("False, None")


calc(char_list, args.expressions)
