class ArrayQueue:
    """FIFO Queue implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty queue."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        self._data.append(e)  # new item stored at end of list

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]  # the last item in the list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.pop(0)  # remove last item from list


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(5)
    q.enqueue(3)
    # print(q._data)
    print(len(q))
    print(q.dequeue())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())
    # # print(q.dequeue())
    # print(q.enqueue(7))
    # print(q.enqueue(9))
    print(q.first())
    # print(q.enqueue(4))
    # print(len(q))
    # print(q.dequeue())