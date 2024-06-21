def selection_sort(a_list):
    for full in range(len(a_list)-1):
        max_num = 0
        for i in range(len(a_list)-full):
            if a_list[i] > a_list[max_num]:
                max_num = i
        a_list[max_num], a_list[i] = a_list[i], a_list[max_num]
    return a_list


if __name__=="__main__":
    a_list = [3, 2, 1, 4, 5, 13, 7, 8, 12, 10]
    print(selection_sort(a_list))