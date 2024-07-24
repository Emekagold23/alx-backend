#!/usr/bin/python3
"""
Create BasicCache class module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Define BasicCache
    """

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key
        """
        return self.cache_data.get(key)
