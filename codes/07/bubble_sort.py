def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                
        print(a_list)


if __name__ == "__main__":
    a_list = [23, 1, 34, 56, 3, 19]
    print(a_list)
    bubble_sort(a_list)
    print(a_list)