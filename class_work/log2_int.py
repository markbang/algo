# 在只使用加法和整数除法的情况下，描述一个递归算法，来计算以 2为底的 n 的对数的整数部分


def log2_int(n):
    if n == 1:
        return 0
    else:
        return 1 + log2_int(n // 2)


if __name__ == "__main__":
    print(log2_int(16))  # 4
    print(log2_int(32))  # 5
    print(log2_int(64))  # 6
    print(log2_int(128))  # 7
    print(log2_int(256))  # 8
    print(log2_int(512))  # 9
    print(log2_int(1024))  # 10
