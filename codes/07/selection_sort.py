def selection_sort(a_list):
    for fill_slot in range(len(a_list)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location

        a_list[fill_slot], a_list[position_of_max] = a_list[position_of_max], a_list[fill_slot]

        # temp = a_list[fill_slot]
        # a_list[fill_slot] = a_list[position_of_max]
        # a_list[position_of_max] = temp


if __name__ == "__main__":
    a_list = [23, 1, 34, 56, 3, 19]
    print(a_list)
    selection_sort(a_list)
    print(a_list)