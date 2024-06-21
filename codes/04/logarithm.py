def algorithm1(N):
    count = 0
    i = N
    while i > 1:
        i = i / 2
        count += 1
    return count


def algorithm2(N):
    count = 0
    i = N
    a = 3
    while i > 1:
        i = i / a
        count += 1
    return count