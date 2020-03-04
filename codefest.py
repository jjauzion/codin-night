def is_possible(map_, position):
    if map_[position] != ".":
        return False
    elif position < len(map_) and map_[position + 1] == "#":
        return True
    elif position > 0 and map_[position - 1] == "#":
        return True
    else:
        return False


def is_finish(map_):
    if "." not in map_:
        return True
    return False


def count_possible(map_):
    cpt = 0
    for i, c in enumerate(map_):
        if is_possible(map_, i):
            cpt += 1
    return cpt


def get_next_map(map_):
    for i, c in enumerate(map_):
        if is_possible(map_, i):
            map_[i] = "#"
            return map_, i
    return None, None


def solve(map_, cpt, l_visited):
    solution = []
    while not is_finish(map_):
        position, map_ = get_next_map(map_)
        solution.append(position)


if __name__ == "__main__":
    map_ = ".#.."
    size = 4
    map_ = list(map_)
    # solve(map_, size)
