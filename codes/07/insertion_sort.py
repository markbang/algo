def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1
        a_list[position] = current_value



if __name__ == "__main__":
    a_list = [23, 1, 34, 56, 3, 19]
    print(a_list)
    insertion_sort(a_list)
    print(a_list)