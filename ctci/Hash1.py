# print(getHash('March 6'))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        print(h)

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h];


t = HashTable()
t.add('march 6', 123)
print(t.arr)
print(t.get('march 6'))