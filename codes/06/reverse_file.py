from array_stack import ArrayStack

def reverse_file(filename):
    S = ArrayStack()

    with open(filename, 'r') as fp:
        for line in fp.readlines():
            S.push(line)

    with open(filename, 'w') as fw:
        while not S.is_empty():
            fw.write(S.pop())


if __name__ == "__main__":
    filename = 'test.txt'
    reverse_file(filename)


    # S = ArrayStack()
    # original = open(filename)
    # for line in original:
    #     S.push(line.rstrip('\n'))
    # original.close()

    # output = open(filename, 'w')
    # while not S.is_empty():
    #     output.write(S.pop() + '\n')
    # output.close()


# if __name__ == "__main__":
#     filename = 'test.txt'
#     reverse_file(filename)