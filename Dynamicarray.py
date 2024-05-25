class DynamicArray:
    def __init__(self, factor=2):
        self.data = []
        self.factor = factor

    def insert_at_index(self, index, element):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete_at_index(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        del self.data[index]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def rotate(self, k):
        if len(self.data) == 0:
            return
        k %= len(self.data)
        self.data = self.data[-k:] + self.data[:-k]

    def reverse(self):
        self.data = self.data[::-1]

    def append(self, element):
        self.data.append(element)

    def prepend(self, element):
        self.data = [element] + self.data

    def merge(self, other):
        self.data.extend(other.data)

    def interleave(self, other):
        result = []
        min_len = min(len(self.data), len(other.data))
        for i in range(min_len):
            result.append(self.data[i])
            result.append(other.data[i])
        result.extend(self.data[min_len:])
        result.extend(other.data[min_len:])
        self.data = result

    def find_middle(self):
        if not self.data:
            return None
        return self.data[len(self.data) // 2]

    def find_index_of(self, element):
        for i, val in enumerate(self.data):
            if val == element:
                return i
        return -1

    def split_at_index(self, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        first = DynamicArray(factor=self.factor)
        first.data = self.data[:index]
        second = DynamicArray(factor=self.factor)
        second.data = self.data[index:]
        return first, second

    def resize(self):
        new_capacity = self.factor * len(self.data)
        self.data += [None] * (new_capacity - len(self.data))
