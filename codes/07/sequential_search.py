def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    print(sequential_search(a_list, 31))
