def shell_sort(a_lsit):
    sub_list_count = len(a_lsit) // 2
    while sub_list_count > 0:
        for start_position in range(sub_list_count):
            gap_insertion_sort(a_lsit, start_position, sub_list_count)
        print("After increments of size", sub_list_count, "The list is", a_lsit)
        sub_list_count = sub_list_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


if __name__ == "__main__":
    a_list = [3, 31, 1, 56, 5, 13, 76, 8, 12, 10]
    shell_sort(a_list)
    print(a_list)
