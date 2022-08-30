class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [[0] for i in range(self.size)]
    
    def hash_function(self, data):
        return data%self.size
    
