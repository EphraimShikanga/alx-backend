#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.orderd_cache_keys = []
    
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
            if key in self.orderd_cache_keys:
                self.orderd_cache_keys.remove(key)
            self.orderd_cache_keys.append(key)
        
        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key = self.orderd_cache_keys[0]
            del self.cache_data[lru_key]
            self.orderd_cache_keys = self.orderd_cache_keys[1:]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        if key in self.orderd_cache_keys:
            self.orderd_cache_keys.remove(key)
        self.orderd_cache_keys.append(key)
        return self.cache_data[key]