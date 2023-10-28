#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching class

    Args:
        BaseCaching (class): BaseCaching class

    Methods:
        def __init__(self): Initializes the LIFOCache instance
        def put(self, key, item)
        def get(self, key):
    """
    def __init__(self):
        super().__init__()
        self.oderd_cache_key = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.oderd_cache_key.append(key)
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lifo_key = self.oderd_cache_key[-1]
            del self.cache_data[lifo_key]
            self.oderd_cache_key = self.oderd_cache_key[:-1]
            print(f"DISCARD: {lifo_key}")
        

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        return self.cache_data.get(key, None)
