class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(-1, 4)
    print(p1)
    print(p2)
    print(p1 + p2)