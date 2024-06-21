import time


def log_2_n(n):
    if n == 1:
        return 0
    if n < 1:
        return log_2_n(n*2) + 1
    else:
        return log_2_n(n//2) + 1


start_time = time.time()
t = log_2_n(2**997+11111)
print(t)
end_time = time.time()
print(start_time)
print(end_time)
print(end_time-start_time)