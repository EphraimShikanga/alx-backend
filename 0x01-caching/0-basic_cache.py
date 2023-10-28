#!/usr/bin/env python3
"""
A basic caching implementation that stores key-value pairs
in memory.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching implementation that stores key-value pairs
    in memory.

    This class inherits from the BaseCaching class and
    implements the put and get methods.
    """
    def put(self, key, item):
        """
        Adds key-value pair to the cache data.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item associated with key from the
        cache data.
        """
        return self.cache_data.get(key, None)
