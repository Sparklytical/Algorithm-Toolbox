# python3

def money_change(money):
    assert 0 <= money <= 10 ** 3
    total = 0
    if money < 5:
        total = money
    elif money < 10:
        total = 1 + (money % 5)
    else:
        total = money // 10
        money = money % 10
        total += money // 5 + money % 5

    return total


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
