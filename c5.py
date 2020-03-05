def get_number(l_n, index, length):
    if index + length <= len(l_n):
        return int("".join(l_n[index:index + length]))
    else:
        tmp = "".join(l_n[index:])
        reste = length - (len(l_n) - index)
        tmp += "".join(l_n[:reste])
        return int(tmp)


def get_best_index(l_n):
    i = 0
    nb = -1
    len_ = 1
    index = 0
    while i < len(l_n):
        tmp = get_number(l_n, i, len_)
        if tmp >= nb:
            nb = tmp
            index = i
        else:
            len_ += 1
            nb = get_number(l_n, index, len_)
        i += 1
    return index


def get_all_nb_(s_n):
    all_nb = []
    for i in range(10):
        n = [str((int(c) + i) % 10) for c in s_n]
        all_nb.append(n)
    return all_nb


def maxScore(counter):
    max_c = counter
    counter = str(counter)
    all_counter = get_all_nb_(counter)
    for c in all_counter:
        i = get_best_index(l_n=c)
        max_c = max(max_c, get_number(c, i, len(c)))
    return max_c


if __name__ == "__main__":
    n = 8279101235
    max_c = maxScore(n)
    print(max_c)
    assert 9890136057 == max_c
    n = 7324707115
    max_c = maxScore(n)
    print(max_c)
    assert 9935102585 == max_c
