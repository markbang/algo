def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


if __name__ == "__main__":
    # a_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    # print(ordered_sequential_search(a_list, 93))
    a_list = list(range(100000000))
    print(ordered_sequential_search(a_list, 9999999))
