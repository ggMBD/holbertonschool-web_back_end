#!/usr/bin/env python3
"""
Module for LIFOCache class.
Implements a caching system using the
Last In First Out (LIFO) eviction policy.
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements
    a caching system with a LIFO eviction policy.
    When the cache is full, the most recently inserted item is discarded.
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        Calls parent init and sets up an OrderedDict
        to track insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """
        Store an item in the cache using LIFO eviction.

        Args:
            key: The key to store the value under.
            value: The value to store in the cache.

        If the cache exceeds MAX_ITEMS, the most recently inserted
        item is discarded. Does nothing if key or value is None.
        """
        if key is None or value is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)

        self.cache_data[key] = value

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with key, or None if the key
            doesn't exist or if key is None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
