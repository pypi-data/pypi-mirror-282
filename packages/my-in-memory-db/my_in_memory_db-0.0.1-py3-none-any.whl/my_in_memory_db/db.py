# my_in_memory_db/db.py
class InMemoryDatabase:
    def __init__(self):
        self.db = {}
        self.transaction_db = None  # Temporary storage for transactions

    def set(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if self.transaction_db is not None:
            self.transaction_db[key] = value
        else:
            self.db[key] = value

    def get(self, key):
        if self.transaction_db is not None and key in self.transaction_db:
            return self.transaction_db.get(key, "Key not found.")
        return self.db.get(key, "Key not found.")

    def delete(self, key):
        if self.transaction_db is not None:
            if key in self.transaction_db:
                del self.transaction_db[key]
            else:
                return "Key not found."
        else:
            if key in self.db:
                del self.db[key]
            else:
                return "Key not found."

    def size(self):
        if self.transaction_db is not None:
            return len(self.transaction_db)
        return len(self.db)

    def begin_transaction(self):
        if self.transaction_db is None:
            self.transaction_db = self.db.copy()
        else:
            raise Exception("Transaction already in progress.")

    def commit_transaction(self):
        if self.transaction_db is not None:
            self.db = self.transaction_db
            self.transaction_db = None
        else:
            raise Exception("No transaction in progress.")

    def rollback_transaction(self):
        if self.transaction_db is not None:
            self.transaction_db = None
        else:
            raise Exception("No transaction in progress.")

