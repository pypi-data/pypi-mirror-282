# tests/test_db.py
import unittest
from my_in_memory_db import InMemoryDatabase

class TestInMemoryDatabase(unittest.TestCase):
    def test_set_and_get(self):
        db = InMemoryDatabase()
        db.set("Canada", 5000)
        self.assertEqual(db.get("Canada"), 5000)

    def test_size(self):
        db = InMemoryDatabase()
        db.set("Canada", 5000)
        self.assertEqual(db.size(), 1)

    def test_delete(self):
        db = InMemoryDatabase()
        db.set("Canada", 5000)
        db.delete("Canada")
        self.assertEqual(db.get("Canada"), "Key not found.")
        self.assertEqual(db.size(), 0)

    def test_transaction(self):
        db = InMemoryDatabase()
        db.set("key1", 100)
        db.begin_transaction()
        db.set("key1", 200)
        self.assertEqual(db.get("key1"), 200)
        db.rollback_transaction()
        self.assertEqual(db.get("key1"), 100)
        db.begin_transaction()
        db.set("key1", 300)
        db.commit_transaction()
        self.assertEqual(db.get("key1"), 300)

if __name__ == '__main__':
    unittest.main()

