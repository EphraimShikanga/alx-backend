#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching class
    """
    def __init__(self):
        super().__init__()
        self.orderd_cache_keys = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.orderd_cache_keys:
                self.orderd_cache_keys.remove(key)
            self.orderd_cache_keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            mru_key = self.orderd_cache_keys[-1]
            del self.cache_data[mru_key]
            self.orderd_cache_keys = self.orderd_cache_keys[:-1]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        if key in self.orderd_cache_keys:
            self.orderd_cache_keys.remove(key)
        self.orderd_cache_keys.append(key)
        return self.cache_data[key]
