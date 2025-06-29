def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = True
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_num = pass_num - 1


if __name__ == "__main__":
    a_list = [23, 1, 34, 56, 3, 19]
    print(a_list)
    short_bubble_sort(a_list)
    print(a_list)
