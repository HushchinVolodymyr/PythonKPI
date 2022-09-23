import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W",  type=int, help='copacity of knapsack')
parser.add_argument("-w", type=int, nargs='+', help='wight of bars')
parser.add_argument("-n", type=int, help='count of bars')

args = parser.parse_args()

copacity = args.W
value_bars = list(args.w)
weight = value_bars
amount_bars = args.n

print(copacity, weight, value_bars, amount_bars)

def knapSack(copacity, weight, value_bars, amount_bars):
    K = [[0 for x in range(copacity + 1)] for x in range(amount_bars + 1)]

    for i in range(amount_bars + 1):
        for w in range(copacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value_bars[i - 1]
                              + K[i - 1][w - weight[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[amount_bars][copacity]

print(knapSack(copacity, weight, value_bars, amount_bars))
