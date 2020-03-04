def digit(n):
    if n == 0:
        return "0"
    baton = n // 5
    point = n % 5
    return "|" * baton + "." * point


def decimalToMaya(n):
    maya_nb = []
    while n >= 20:
        reste = n % 20
        maya_nb.append("{}".format(digit(reste)))
        n = n // 20
    maya_nb.append("{}".format(digit(n)))
    return " ".join(maya_nb[::-1])


if __name__ == "__main__":
    print(decimalToMaya(18))
    print(decimalToMaya(20))
    print(decimalToMaya(26))
    print(decimalToMaya(457))
