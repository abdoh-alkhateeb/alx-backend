#!/usr/bin/env python3
"""
Defines `LFUCache`.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching system.
    """

    def __init__(self):
        super().__init__()
        self.map = dict()

    def put(self, key, item):
        """
        Sets a key to a given value.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            freq = self.map.pop(key)
            self.map[key] = freq + 1

            self.cache_data[key] = item
            return

        if len(self.map) == self.MAX_ITEMS:
            min_freq = min(self.map.values())
            keys = [k for k, v in self.map.items() if v == min_freq]

            del_key = keys.pop(0)

            del self.map[del_key]
            del self.cache_data[del_key]

            print("DISCARD:", del_key)

        self.map[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value for a given key.
        """
        if key is None or key not in self.cache_data:
            return None

        freq = self.map.pop(key)
        self.map[key] = freq + 1

        return self.cache_data[key]
