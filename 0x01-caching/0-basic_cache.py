#!/usr/bin/env python3
"""
Defines `BasicCache`.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system that doesn't have limit.
    """

    def put(self, key, item):
        """
        Sets a key to a given value.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value for a given key.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
