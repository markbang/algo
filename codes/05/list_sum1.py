def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i

    return the_sum


if __name__ == "__main__":
    num_list = [1, 3, 5, 7, 9]
    print(list_sum(num_list))