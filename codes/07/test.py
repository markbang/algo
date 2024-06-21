def put(self, key, data):
    hash_value = self.hash_function(key, len(self.slots))

    if self.slots[hash_value] == None:
        self.slots[hash_value] = key
        self.data[hash_value] = data
    else:
        if self.slots[hash_value] == key:
            self.data[hash_value] = data  # replace the old data
        else:
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))
            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data # replace the old data