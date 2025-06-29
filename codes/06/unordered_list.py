from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def look(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    # def search(self, item):
    #     current = self.head
    #     found = False
    #     while current != None and not found:
    #         if current.get_data() == item:
    #             found = True
    #         else:
    #             current = current.get_next()
    #     return found

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
        pass

    def insert(self, pos, item):
        pass

    def index(self, item):
        pass

    def pop(self, item, pos=None):
        pass


if __name__ == "__main__":
    my_list = UnorderedList()
    print(my_list.is_empty())
    print("The current length", my_list.length())
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    print("The current length", my_list.length())
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list.is_empty())
    print("The current length", my_list.length())
    my_list.look()
    # print(my_list.is_empty())
    # print(my_list.length())
    print(my_list.search(93))
    print("-" * 10)
    my_list.remove(26)
    my_list.look()
    print("-" * 10)
    my_list.remove(54)
    my_list.look()
    print("-" * 10)
    my_list.remove(31)
    my_list.look()
    print("-" * 10)
    # print(my_list.is_empty())
    # print(my_list.length())
    # print(my_list.remove(54))
    # print(my_list.is_empty())
    # print(my_list.length())


# from node import Node

# class UnorderedList:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head == None

#     def add(self, item):
#         temp = Node(item)
#         temp.set_next(self.head)
#         self.head = temp

#     def length(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             current = current.get_next()
#         return count

#     def search(self, item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 current = current.get_next()
#         return found

#     def remove(self, item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.get_next()

#         if previous == None:
#             self.head = current.get_next()
#         else:
#             previous.set_next(current.get_next())


# if __name__ == "__main__":
#     my_list = UnorderedList()
#     print(my_list.is_empty())
#     print(my_list.length())
#     my_list.add(31)
#     my_list.add(77)
#     print(my_list.is_empty())
#     print(my_list.length())
#     my_list.add(17)
#     my_list.add(93)
#     my_list.add(26)
#     my_list.add(54)
#     print(my_list.is_empty())
#     print(my_list.length())
#     print(my_list.search(7))
#     print(my_list.remove(26))
#     print(my_list.is_empty())
#     print(my_list.length())
#     print(my_list.remove(54))
#     print(my_list.is_empty())
#     print(my_list.length())
