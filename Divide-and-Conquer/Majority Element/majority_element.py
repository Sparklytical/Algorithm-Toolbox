# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def get_majority(array):
    if len(array) == 1:
        return array[0]
    left = get_majority(array[:len(array) // 2])
    right = get_majority(array[len(array) // 2:])
    if left == right:
        return left
    else:
        sum_left = sum([1 if array[i] == left else 0 for i in range(len(array))])
        sum_right = sum([1 if array[i] == right else 0 for i in range(len(array))])
        if sum_left > sum_right:
            return left
        return right


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    result = get_majority(elements)
    count = 0
    for i in range(len(elements)):
        if elements[i] == result:
            count += 1
            if count > len(elements) // 2:
                return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
