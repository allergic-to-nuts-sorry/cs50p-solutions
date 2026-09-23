class Jar:
    def __init__(self, capacity=12):
        # Uses setters to enforce validation during initialization
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid deposit quantity")
        if (self._size + n) > self._capacity:
            raise ValueError("Capacity Exceeded!")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid withdraw quantity")
        if (self._size - n) < 0:
            raise ValueError("Not enough cookies!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid Jar Capacity")
        if hasattr(self, "_size") and capacity < self._size:
            raise ValueError("Capacity cannot be less than current size")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int) or size < 0:
            raise ValueError("Invalid Size")
        if size > self._capacity:
            raise ValueError("Size cannot exceed capacity")
        self._size = size
