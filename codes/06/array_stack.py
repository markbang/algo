class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.data)

    def __str__(self):
        return " ".join(list(map(str, self.data)))

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception
        else:
            return self.data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception
        return self.data.pop()


if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    print(S)
    S.push(3)
    print(S)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    print(S.pop())

    # def __init__(self):
    #     """Create an empty stack."""
    #     self._data = []

    # def __len__(self):
    #     """Return the number of elements in the stack."""
    #     return len(self._data)

    # def is_empty(self):
    #     """Return True if the stack is empty."""
    #     return len(self._data) == 0

    # def push(self, e):
    #     """Add element e to the top of the stack."""
    #     self._data.append(e)  # new item stored at end of list

    # def top(self):
    #     """Return (but do not remove) the element at the top of the stack.

    #     Raise Empty exception if the stack is empty.
    #     """
    #     if self.is_empty():
    #         raise Empty('Stack is empty')
    #     return self._data[-1]  # the last item in the list

    # def pop(self):
    #     """Remove and return the element from the top of the stack (i.e., LIFO).

    #     Raise Empty exception if the stack is empty.
    #     """
    #     if self.is_empty():
    #         raise Empty('Stack is empty')
    #     return self._data.pop()  # remove last item from list


# class Empty(Exception):
#     """Error attempting to access an element from an empty container."""
#     pass


# if __name__ == "__main__":
#     s = ArrayStack()
#     print(s.is_empty())
#     s.push(4)
#     s.push("dog")
#     print(s.top())
#     s.push(True)
#     print(len(s))
#     print(s.is_empty())
#     s.push(8.4)
#     print(s.pop())
#     print(s.pop())
#     print(len(s))
