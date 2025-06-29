class Deque:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def add_first(self, e):
        return self._queue.insert(0, e)

    def add_last(self, e):
        return self._queue.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._queue.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._queue.pop(-1)

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._queue[0]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._queue[-1]


class Empty(Exception):
    """Error attempting to access an element from an empty container."""


if __name__ == "__main__":
    queue = Deque()
    queue.add_first(5)
    queue.add_last(3)
    queue.add_first(1)
    print(queue.first())
    print(queue.last())
    print(queue.delete_first())
    print(queue.first())
