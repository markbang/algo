class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
        return self.data 
    def set_next(self, new_next):
        self.next = new_next
        return next
    

if __name__ == "__main__":
    temp = Node(93)
    print(temp.get_data())
    print(temp.get_next())
    temp1 = Node(3)
    temp.set_next(temp1)
    print(temp.get_next().get_data())