# agent/memory.py

class ConversationMemory:
    def __init__(self):
        self.data = {
            "age": None,
            "income": None,
            "category": None,
            "state": None,
            "gender": None,
            "student": None,
            "bpl": None,
        }
        self.contradiction = False   # 🔴 NEW

    def update(self, key, value):
        """
        Returns:
        - True  → update successful
        - False → contradiction detected
        """
        old = self.data.get(key)

        if old is not None and old != value:
            self.contradiction = True
            return False   # 🚨 contradiction

        self.data[key] = value
        return True

    def get(self, key):
        return self.data.get(key)

    def is_complete(self):
        return all(v is not None for v in self.data.values())

    def has_contradiction(self):
        return self.contradiction

    def reset(self):
        for k in self.data:
            self.data[k] = None
        self.contradiction = False

    def dump(self):
        return self.data
