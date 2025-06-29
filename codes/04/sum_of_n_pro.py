import time


def sum_of_n_pro(n):
    """计算前n个整数之和"""
    start = time.time()
    the_sum = n * (n + 1) / 2

    end = time.time()

    return the_sum, end - start


if __name__ == "__main__":
    print("Sum is %d required %10.10f seconds" % sum_of_n_pro(10000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_pro(100000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_pro(1000000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_pro(10000000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_pro(100000000))
