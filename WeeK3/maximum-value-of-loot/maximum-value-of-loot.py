# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    value = 0
    normalize = [((a / b), b) for a, b in zip(prices, weights)]
    normalize.sort(key=lambda tup: tup[0], reverse=True)
    for i in normalize:
        if (capacity - i[1]) > 0:
            value += i[0] * i[1]
            capacity -= i[1]
        else:
            value += capacity * i[0]
            break
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
