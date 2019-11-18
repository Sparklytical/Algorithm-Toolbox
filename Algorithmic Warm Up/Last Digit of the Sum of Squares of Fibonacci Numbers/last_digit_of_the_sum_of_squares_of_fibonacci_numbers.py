# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    last_n = fibonacci_number_again(n, 10)
    last_n1 = fibonacci_number_again(n + 1, 10)
    return last_n * last_n1 % 10


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n
    else:
        prev = 0
        current = 1
        counter = 2
        sequence = [0, 1]
        for i in range(2, n + 1):
            f = prev + current
            prev = current
            current = f
            if prev % m == 0 and current % m == 1:
                counter -= 1
                break
            else:
                counter += 1
                sequence.append(current % m)
        reminder = n % counter
        return sequence[reminder]


if __name__ == "__main__":
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
