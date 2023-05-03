import unittest
from sep_chain_ht import MyHashTable

class TestMyHashTable(unittest.TestCase):

    def test_insert(self):
        ht = MyHashTable()
        ht.insert(1, 'a')
        ht.insert(12, 'b')
        ht.insert(23, 'c')
        self.assertEqual(ht.get(1), 'a')
        self.assertEqual(ht.get(12), 'b')
        self.assertEqual(ht.get(23), 'c')

    def test_insert_collision(self):
        ht = MyHashTable(table_size=5)
        ht.insert(1, 'a')
        ht.insert(6, 'b')
        ht.insert(11, 'c')
        self.assertEqual(ht.collisions(), 1)
        self.assertEqual(ht.get(1), 'a')
        self.assertEqual(ht.get(6), 'b')
        self.assertEqual(ht.get(11), 'c')

    def test_remove(self):
        ht = MyHashTable()
        ht.insert(1, 'a')
        ht.insert(12, 'b')
        ht.insert(23, 'c')
        ht.remove(12)
        self.assertEqual(ht.size(), 2)
        with self.assertRaises(LookupError):
            ht.get(12)

    def test_resize(self):
        ht = MyHashTable(table_size=5)
        for i in range(10):
            ht.insert(i, str(i))
        self.assertEqual(ht.size(), 10)
        self.assertEqual(ht.table_size, 23)

if __name__ == '__main__':
    unittest.main()
