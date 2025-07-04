from array_stack import ArrayStack


def divide_by_2(dec_number):
    rem_stack = ArrayStack()
    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


if __name__ == "__main__":
    dec_number = 4
    print(divide_by_2(dec_number))
