# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    idx = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[idx]:
            idx = i
    temp = numbers[-1]
    numbers[-1] = numbers[idx]
    numbers[idx] = temp
    idx = 0

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[idx]:
            idx = i
    temp = numbers[-2]
    numbers[-2] = numbers[idx]
    numbers[idx] = temp

    return numbers[-1] * numbers[-2]


if __name__ == "__main__":
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
