def binary_search_r(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid_point = len(a_list) // 2
        if a_list[mid_point] == item:
            return True
        else:
            if item < a_list[mid_point]:
                return binary_search_r(a_list[:mid_point], item)
            else:
                return binary_search_r(a_list[mid_point + 1 :], item)


if __name__ == "__main__":
    a_list = list(range(100000000))
    item = 9999999
    print(binary_search(a_list, item))
