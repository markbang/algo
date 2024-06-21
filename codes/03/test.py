import copy

a = [1, 2, 3]
b = [4, 5, 6]

test1 = [a, b]
# test2 = test1
# test2 = list(test1)
# test2 = copy.copy(test1)
test2 = copy.deepcopy(test1)

test1[1][1] = 10
print(test1)
print(test2)