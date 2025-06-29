from Node import Node


class UnordredList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(Node(item))

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        while count != pos:
            count += 1
            previous = current
            current = current.get_next()
        insert_item = Node(item)
        insert_item.set_next(current)
        previous.set_next(insert_item)

    def index(self, item):
        current = self.head
        count = 0
        while current.get_data() != item:
            if current.get_next() == None:
                return "Not Found"
            else:
                count += 1
                current = current.get_next()
        return count

    def pop(self, pos=None):
        if pos == None:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            return current.get_data()
        else:
            current = self.head
            previous = None
            count = 0
            while count != pos:
                count += 1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            return current.get_data()

    def __str__(self) -> str:
        current = self.head
        result = []
        while current != None:
            result.append(current.get_data())
            current = current.get_next()
        return "-->".join(map(str, result)) + "-->None"


if __name__ == "__main__":
    ordered_list = UnordredList()
    print(ordered_list.is_empty())
    ordered_list.add(3)
    ordered_list.add(5)
    ordered_list.add(7)
    ordered_list.add(9)
    print(ordered_list)
    print(ordered_list.length())
    print(ordered_list.search(5))
    print(ordered_list.search(10))
    ordered_list.remove(5)
    print(ordered_list)
    ordered_list.append(5)
    print(ordered_list)
    ordered_list.insert(2, 6)
    print(ordered_list)
    print(ordered_list.index(6))
    print(ordered_list.pop())
    print(ordered_list)
    print(ordered_list.pop(2))
    print(ordered_list)
    print(ordered_list.is_empty())
