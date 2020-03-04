import math


def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def calcDistance(checkpoints):
    checkpoints = sorted(checkpoints, key=get_x)
    d = 0
    for i in range(len(checkpoints)):
        if i == 0: continue
        d += dist(checkpoints[i - 1], checkpoints[i])
    return d


def get_x(p1):
    return p1[0]


l_p = [[1, 10], [-1, 5], [4, 6]]
d = calcDistance(l_p)
print(d)
