#python3
def min_refills(n, a, dist_with_full_tank):
    num_refills = 0
    current_refills = 0
    last_refills = 0
    while current_refills <= (n):
        last_refills = current_refills
        while (current_refills <= n and (a[current_refills + 1] - a[last_refills]) <= dist_with_full_tank):
                current_refills = current_refills + 1

        
        if current_refills == last_refills:
            return -1
        if current_refills <= n:
            num_refills = num_refills + 1
    return num_refills

def start():
    B = int(input())
    L = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0,0)
    a.append(B)
    n = n
    print(min_refills(n, a, L))

if __name__ == "__main__":
    start()