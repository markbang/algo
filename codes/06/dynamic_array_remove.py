def remove(self, value):
    """Remove frist occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version.
    for k in range(self._n):
        if self._A[k] == value:  # found a match!
            for j in range(k, self._n - 1):  # shift others to fill gap
                self._A[j] = self._A[j + 1]
            self._A[self._n - 1] = None  # help garbage collection
            self._n -= 1  # we have one less item
            return  # exit immediately
    raise ValueError("value not found.")  # only reached if no match
