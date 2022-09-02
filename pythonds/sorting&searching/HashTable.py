class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [[0] for i in range(self.size)]
    
    def hash(self, data):
        return data%self.size
    
    def rehash(self, old_hash):
        # Collision resolution: Linear Probing
        return (old_hash+1)%self.size
    
    def put(self, key, val):
        hash_value = self.hash(key, val)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = val
        else:
            # update the val if key is already taken
            if self.slots[hash_value] == key:
                self.data[hash_value] = val
            else:
                next_pos = self.rehash(hash_value)
                # loop next_pos is not found either empty or key exists in the table
                while self.slots[next_pos] != None and self.slots[next_pos] != key:
                    next_pos = self.rehash(next_pos)
                
                if self.slots[next_pos] == None:
                    self.slots[next_pos] = key
                    self.data[next_pos] = val
                else:
                    # element already exists and update the val
                    self.data[next_pos] = val
        
                

    
    
