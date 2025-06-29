"""
任意对象，只要定义了__next__方法，它就是一个迭代器。
class Iterator:

    def __next__(self):
        return self


if __name__ == '__main__':
    print(Iterator())
"""


class Iterator:
    def __init__(self, squence):
        self._seq = squence
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index < len(self._seq):
            return self._seq[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == "__main__":
    a = Iterator([1, 2, 3, 4, 5])
    print(next(a), next(a))
    n = 2
    for i in a:
        print(i, end=" ")
        n += 1
