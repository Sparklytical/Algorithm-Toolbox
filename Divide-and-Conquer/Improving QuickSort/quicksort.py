# python3

from random import randint


def partition3(array, left, right):
    pivot = array[left]
    i, j = left, right
    while i <= j:
        while array[i] < pivot: i += 1
        while array[j] > pivot: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    return j, i


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1)
    randomized_quick_sort(array, m2, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # quicksort(elements, 0, len(elements)-1)
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(" ".join(map(str, elements)))
