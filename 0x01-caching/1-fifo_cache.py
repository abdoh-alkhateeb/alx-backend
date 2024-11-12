#!/usr/bin/env python3
"""
Defines `FIFOCache`.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system.
    """

    def __init__(self):
        super().__init__()
        self.q = list()

    def put(self, key, item):
        """
        Sets a key to a given value.
        """
        if key is None or item is None:
            return

        if len(self.q) == self.MAX_ITEMS:
            del_key = self.q.pop(0)
            del self.cache_data[del_key]

            if key != del_key:
                print("DISCARD:", del_key)

        self.q.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value for a given key.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
