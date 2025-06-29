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
