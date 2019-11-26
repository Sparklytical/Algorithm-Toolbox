# Uses python3
import sys

def optimal_summands(n):
    summands = []
    new_n=n
    for i in range(1,n+1):
        if (i+1)>new_n-i:
            summands.append(new_n)
            break
        else:
            summands.append(i)
            new_n-=i
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')