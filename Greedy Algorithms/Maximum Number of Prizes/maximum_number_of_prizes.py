# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    new_n = n
    for i in range(1, n + 1):
        if (i + 1) > new_n - i:
            summands.append(new_n)
            break
        else:
            summands.append(i)
            new_n -= i
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
    