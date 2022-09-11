from tracemalloc import start


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, data):
        return data % self.size

    def rehash(self, old_hash):
        # Collision resolution: Linear Probing
        return (old_hash + 1) % self.size

    def put(self, key, val):
        hash_value = self.hash(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = val
        else:
            # update the val if key is already taken
            if self.slots[hash_value] == key:
                self.data[hash_value] = val
            else:
                next_pos = self.rehash(hash_value)
                # loop next_pos is not found either empty or key exists in the
                # table
                while self.slots[next_pos] is not None and self.slots[next_pos] != key:
                    next_pos = self.rehash(next_pos)

                if self.slots[next_pos] is None:
                    self.slots[next_pos] = key
                    self.data[next_pos] = val
                else:
                    # element already exists and update the val
                    self.data[next_pos] = val

    def get(self, key):
        start_slot = self.hash(key)
        next_pos = start_slot
        while self.slots[next_pos] != key:
            next_pos = self.rehash(next_pos)
            if start_slot == next_pos:
                return None
        return self.data[next_pos]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        return self.put(key, val)

    def display(self):
        print(self.slots)
        print(self.data)


if __name__ == "__main__":
    hash_map = HashTable(20)
    hash_map[0] = 15
    hash_map[146] = 11
    hash_map[201] = 111
    hash_map[60] = 191
    hash_map[80] = 291
    hash_map[100] = 219
    hash_map[1] = 22
    hash_map.display()
    print(hash_map[10])
    print(hash_map[1])
