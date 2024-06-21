class Deque:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data.pop()

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[-1]

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


if __name__ == "__main__":
    d = Deque()
    d.add_last(5)
    print(d._data)
    d.add_first(3)
    print(d._data)
    d.add_first(7)
    print(d._data)
    print(d.first())
    d.delete_last()
    print(d._data)
    print(len(d))
    d.delete_last()
    print(d._data)
    d.delete_last()
    print(d._data)
    d.add_first(6)
    print(d.last())
    d.add_first(8)
    print(d.is_empty())
    print(d.last())
