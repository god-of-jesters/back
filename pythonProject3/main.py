def beeramid(bonus, price):
    beer_can = bonus // price
    i = 1
    level = 0
    while beer_can - i ** 2 >= 0:
        beer_can -= i ** 2
        level += 1
        i += 1
    print(level)


def reverse_number(n):
    if n < 0:
        l = [i for i in str(n)][1:]
        l.reverse()
        s = -int("".join(l))
        return s
    else:
        l = [i for i in str(n)]
        l.reverse()
        s = int("".join(l))
        return s


print(reverse_number(-123))
