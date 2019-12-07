# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(a, b):
    i, j, count = 0, 0, 0
    result = []
    while i + j < len(a) + len(b):
        # print(a, b, i)
        if j >= len(b) or (i < len(a)) and a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            if i < len(a):
                count += len(a) - i
            result.append(b[j])
            j += 1
    return result, count


def mergesort(a):
    if len(a) == 1:
        return a, 0
    b, b_count = mergesort(a[:len(a) // 2])
    c, c_count = mergesort(a[len(a) // 2:])
    result, count = merge(b, c)
    return result, count + b_count + c_count


def compute_inversions(a):
    _, count = mergesort(a)
    return count  # [0 1 0 1 0 1 0 0 0 1]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
