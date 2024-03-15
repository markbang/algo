# This is a test file for class and object in Python
class CreditCard:
    
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
  
    def set_limit(self, limit):
        self._limit = limit
    
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        self._balance -= amount
        

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # change add
    def __add__(self, other):
        return "Point(x:%d, y:%d)" % (self.x + other.x, self.y + other.y)
    # change print
    def __str__(self):
        return "Point(x:%s, y:%s)" % (self.x, self.y)
           

class Vector:
    
    def __init__(self, d):
        self._coords = [0] * d
        
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
        
    def __str__(self):
        return '[' + str(self._coords)[1:-1] + ']'
    
    def __eq__(self, other):
        return self._coords == other._coords

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

          
if __name__ == '__main__':
    pass