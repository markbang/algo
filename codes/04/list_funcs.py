from timeit import Timer

def test1():
    l = []
    for i in range(10000): # 1000
        l = l + [i]

def test2():
    l = []
    for i in range(10000): # 1000
        l.append(i)

def test3():
    l = [i for i in range(10000)] # 1000

def test4():
    l = list(range(10000)) # 1000

# timeit模块使Python开发人员能够在一致的环境下运行函数，并且在多种操作系统下使用尽可能相似的机制，以实现跨平台计时。

# timeit模块这么做，是为了在一个干净的环境中运行计时测试，以免某些变量以某种意外的方式干扰函数的性能。

if __name__ == "__main__":
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print("append ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer("test3()", "from __main__ import test3") 
    print("comprehension ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer("test4()", "from __main__ import test4") 
    print("list range ", t4.timeit(number=1000), "milliseconds")
