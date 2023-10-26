from base_caching import BaseCaching
from collections import OrderedDict

class LIFOCache(BaseCaching):
    def __init__(self):
        self.cache_data = OrderedDict()
        return super().__init__()
    def put(self, key, item):
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            self.cache_data.pop(keys[-1])
            print(f"DISCARD: {keys[-1]}")
        if key is None or item is None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        return self.cache_data.get(key, None)