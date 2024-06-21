def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)


if __name__ == "__main__":
    n = 10
    output = f(n)
    print(output)