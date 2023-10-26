from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching class
    """
    def __init__(self):
        """
        Initializes the FIFOCache instance
        """
        self.cache_data = OrderedDict()
        return super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            self.cache_data.pop(keys[0])
            print(f"DISCARD: {keys[0]}")
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        return self.cache_data.get(key, None)
