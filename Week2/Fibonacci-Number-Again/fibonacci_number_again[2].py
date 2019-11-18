# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    arr = [0, 1]
    current = 1
    previous = 1
    index = 2

    while True:
        new = arr[index - 1] + arr[index - 2]
        arr.append(new % m)
        previous = current
        current = arr[index]
        index += 1
        if current == 1 and previous == 0:
            arr.pop()
            arr.pop()
            break
        return arr


if __name__ == "__main__":
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
