class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return j-th coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set j-th coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    # def __ne__(self, other):
    #     """Return True if vector differs from other."""
    #     return not self == other    # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"  # adapt list representation


if __name__ == "__main__":
    v = Vector(10)
    print(len(v))
    print(v[1])
    v[1] = 10
    print(v[1])

    print(v)
    v2 = Vector(10)
    v2[3] = 22

    print(v)
    print(v2)

    print(v + v2)
