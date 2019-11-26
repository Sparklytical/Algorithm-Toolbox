# Uses python3

import sys


def IsGreaterOrEqual(a, b):
    if (a + b) > b + a:
        return True
    else:
        return False
    # a=list(a)
    # b=list(b)
    #
    # if len(a)<=len(b):
    #     long=b
    #     short=a
    #     T=True
    #     F=False
    # else:
    #     long=a
    #     short=b
    #     T=False
    #     F=True
    #
    # flag=False
    #
    # for x in short:
    #     for y in long:
    #         print("a: ",x,"b: ",y,x<y)
    #         if(x>y):
    #             return T
    #         if(x==y):
    #             flag = T
    #             long.remove(y)
    #             break;
    #         else:
    #             return F
    # return flag


def largest_number(digits):
    res = ""

    while (digits):
        maxdigit = "0"
        for digit in digits:
            # print("Digit: ",digit, "Maxdigit: ",maxdigit)
            if IsGreaterOrEqual(digit, maxdigit):
                maxdigit = digit
                # print("maxdigit: ", maxdigit)
        res += maxdigit
        digits.remove(maxdigit)

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
