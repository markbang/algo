def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this version)
    if self._n == self._capacity:  # not enough room
        self._resize(2 * self._capacity)  # do double capacity
    for j in range(self._n, k, -1):  # shift rightmost first
        self._A[j] = self._A[j - 1]
    self._A[k] = value  # store newest element
    self._n += 1
