# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index : to_index + 1]) % 10


def get_pisano_sequence(n):
    """This Function calculates the Pisano Period"""
    arr = [0, 1]
    current = 1
    previous = 1
    index = 2
    while True:
        new = arr[index - 1] + arr[index - 2]
        arr.append(new % n)
        previous = current
        current = arr[index]
        index += 1
        if current == 1 and previous == 0:
            arr.pop()
            arr.pop()
            break
    return arr


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    arr = get_pisano_sequence(10)
    sum = 0
    for i in range(a % 60, b % 60 + 1):
        sum = sum + arr[i]
    return sum % 10


if __name__ == "__main__":
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
