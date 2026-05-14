#!/usr/bin/env python3
"""
Module for FIFOCache class.
Implements a caching system using the
First In First Out (FIFO) eviction policy.
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements
    a caching system with a FIFO eviction policy.
    When the cache is full, the oldest inserted item is discarded.
    """

    def __init__(self):
        """
        Initialize the FIFO cache.
        Calls parent init and sets up an OrderedDict
        to track insertion order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """
        Store an item in the cache using FIFO eviction.

        Args:
            key: The key to store the value under.
            value: The value to store in the cache.

        If the cache exceeds MAX_ITEMS, the first inserted
        item is discarded. Does nothing if key or value is None.
        """
        if key is None or value is None:
            return

        self.cache_data[key] = value

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

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
