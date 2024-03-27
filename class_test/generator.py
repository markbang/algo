def generator_function():
    l = []
    for i in range(10):
        l.append(i)
    return l

for item in generator_function():
    print(item)