class LRUCache:

    def __init__(self, capacity: int):
        self.t = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        value = self.t.get(key, -1)
        if value == -1: return -1
        self.t.pop(key)
        self.t[key] = value
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.t:
            self.t.pop(key)
        elif len(self.t) == self.capacity:
            self.t.pop(list(self.t.keys())[0])

        self.t[key] = value

        
