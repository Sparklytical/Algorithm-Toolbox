# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    j = len(keys) // 2
    a = 0
    b = len(keys)
    answer = -1
    while a <= b and 0 <= j < len(keys):
        if query == keys[j]:
            answer = j
            break
        if query < keys[j]:
            b = j - 1
            j = (a + b) // 2
        else:
            a = j + 1
            j = (a + b) // 2
    return answer


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))
    input_keys = input_keys[1:]
    input_queries = list(map(int, input().split()))
    input_queries = input_queries[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
