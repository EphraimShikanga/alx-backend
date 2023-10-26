#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
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
        def put(self, key, item):
            """
            Adds an item to the cache
            """
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                self.cache_data.pop(keys[-1])
                print(f"DISCARD: {keys[-1]}")
            if key is None or item is None:
                return
            self.cache_data[key] = item

        def get(self, key):
            """
            Retrieves an item from the cache
            """
            return self.cache_data.get(key, None)
