import ctypes                                       # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n 

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                            # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                # not enough room
            self._resize(2 * self._capacity)         # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                            # nonpublic utitiy
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):                     # new (bigger) array
            B[k] = self._A[k]
        self._A = B                                  # use the bigger array
        self._capacity = c 

    def _make_array(self, c):                        # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()              # see ctypes documentation

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None      # help garbage collection
                self._n -= 1                     # we have one less item
                return                           # exit immediately
        raise ValueError('value not found.')     # only reached if no match

    def insert(self, k, value):
        if self._n == self._capacity:         # not enough room
            self._resize(2 * self._capacity)  # do double capacity
        for j in range(self._n, k, -1):       # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                    # store newest element
        self._n += 1


if __name__ == "__main__":
    dynamic_array = DynamicArray()
    for i in range(10):
        dynamic_array.append(i)
    print(dynamic_array[1])
    dynamic_array.insert(1, 20)
    print(dynamic_array[1])
    dynamic_array.remove(20)
    print(dynamic_array[1])





