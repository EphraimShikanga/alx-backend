#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching class
    """
    def __init__(self):
        """
        Initializes the FIFOCache instance
        """
        super().__init__()
        self.orderd_cache_keys = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            fifo_key = self.orderd_cache_keys[0]
            del self.cache_data[fifo_key]
            self.orderd_cache_keys = self.orderd_cache_keys[1:]
            print(f"DISCARD: {fifo_key}")
        if key and item:
            self.cache_data[key] = item
            if key in self.orderd_cache_keys:
                self.orderd_cache_keys.remove(key)
            self.orderd_cache_keys.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        return self.cache_data.get(key, None)
