
def hannuota(n, A, B, C):
    if n == 1:
        print(A, '移到', C)
    else:
        hannuota(n-1, A, C, B)
        hannuota(1, A, B, C)
        hannuota(n-1, B, A, C)


if __name__ == '__main__':
    hannuota(4, '塔A', '塔B', '塔C')