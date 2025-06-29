def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return a_list


if __name__ == "__main__":
    a_list = [3, 2, 1, 4, 5, 13, 7, 8, 12, 10]
    print(insertion_sort(a_list))
