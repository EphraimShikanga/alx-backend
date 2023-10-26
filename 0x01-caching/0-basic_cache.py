#!/usr/bin/env python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching implementation that stores key-value pairs
    in memory.

    This class inherits from the BaseCaching class and
    implements the put and get methods.
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
