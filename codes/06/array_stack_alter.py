class ArrayStackAlter:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.insert(0, e)  # new item stored at start of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[0]  # the first item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop(0)  # remove first item from list


class Empty(Exception):
    """Error attempting to access an element from an empty container."""

    pass


if __name__ == "__main__":
    s = ArrayStackAlter()
    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.top())
    s.push(True)
    print(len(s))
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(len(s))
