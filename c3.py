import math


def old_countDigits(n):
    # not ok for 10^10
    l = list(range(1, n + 1))
    s = "".join([str(c) for c in l])
    return len(s)


def mod(n):
    len_ = len(str(n))
    reste = 9 + len_
    div = 10
    len_div = len(str(div))
    while n > div:
        reste += (div * 10 - div) * len_div
        div = div * 10
        len_div += 1
    return reste


def get_order(n):
    return int(math.pow(10, len(str(n)) - 1))


def countDigits(n):
    order = get_order(n)
    nb_order = mod(order)
    return nb_order + len(str(order)) * (n - order)


def countDigits2(n):
    # not ok for 10^10
    i = 0
    cpt = 0
    while i < n:
        i += 1
        cpt += len(str(i))
    return cpt


if __name__ == "__main__":
    print(old_countDigits(10000))
    print(mod(10000))
    print(mod(10))
    print(old_countDigits(2823))
    print(countDigits(2823))
    print(countDigits(int(math.pow(10, 10))))

