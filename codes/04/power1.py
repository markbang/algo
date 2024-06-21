def algorithm(N)
    if N <= 0: return 1
    count_1 = algorithm(N - 1)
    count_2 = algorithm(N - 1)
    return count_1 + count_2