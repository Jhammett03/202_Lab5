class MyHashTable:
    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)]
        self.num_items = 0
        self.num_collisions = 0
        
        

