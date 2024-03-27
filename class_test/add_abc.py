# l = []
# for a in range(1001):
#     for b in range(1001-a):
#         c = 1000-(a+b)
#         if a**2 + b**2 == c**2:
#             l.append([a, b, c])
# print(l)
def sum_of_n(n):
    the_sum = n * (n + 1) / 2
    return the_sum
print(sum_of_n(10))