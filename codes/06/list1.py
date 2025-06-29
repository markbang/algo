import sys  # provides getsizeof function


def list1():
    n = 300
    data = []
    for k in range(n):  # NOTE: must fix choice of n
        a = len(data)  # number of elements
        b = sys.getsizeof(data)  # actual size of bytes
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)  # increse length by one


if __name__ == "__main__":
    list1()
