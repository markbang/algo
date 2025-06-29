class ArrayStack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self) -> str:
        return str(self._stack)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self._stack.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._stack[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._stack.pop()


def reverse_file(filename):
    S = ArrayStack()
    with open(filename, "r") as file:
        for line in file.readlines():
            S.push(line.rstrip("\n"))
    with open(filename, "w") as file:
        while not S.is_empty():
            file.write(S.pop() + "\n")


if __name__ == "__main__":
    reverse_file("basic_strct/test.txt")
