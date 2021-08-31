"""
implementing lru cache

"""

from collections import OrderedDict

class LRUCache:

    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        pass

    def get(self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def put(self,key,val):
        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


    def print_cache(self):
        for item in self.cache.values():
            print(item)


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put(1,5)
    lru_cache.put(2,4)
    lru_cache.put(3,3)
    lru_cache.get(1)
    lru_cache.put(4,6)
    lru_cache.print_cache()
