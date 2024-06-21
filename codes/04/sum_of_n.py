import time

def sum_of_n(n):
    """计算前n个整数之和
    """
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum += i

    end = time.time()

    return the_sum, end-start


if __name__ == '__main__':
    for i in range(5):
        # print("Sum is %d required %10.7f seconds" % sum_of_n(10000))
        # print("Sum is %d required %10.7f seconds" % sum_of_n(100000))
        print("Sum is %d required %10.7f seconds" % sum_of_n(1000000))