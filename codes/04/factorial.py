def algorithm(N):
    if N <= 0:
        return 1
    count = 0
    for _ in range(N):
        count += algorithm(N - 1)
    return count
