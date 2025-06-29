def to_str(n, base):
    conver_string = "0123456789ABCDEF"
    if n < base:
        return conver_string[n]
    else:
        return to_str(n // base, base) + conver_string[n % base]


if __name__ == "__main__":
    for n, base in [(111, 16), (100, 2), (100, 10)]:
        print("n: {}, base: {}, result: {}".format(n, base, to_str(n, base)))
