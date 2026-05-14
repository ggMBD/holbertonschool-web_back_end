#!/usr/bin/env python3
"""
Module for BasicCache class.
Implements a simple caching system with no size limit
and no eviction policy.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements
    a basic caching system with no eviction policy.
    Items are stored indefinitely until manually removed.
    """

    def put(self, key, value):
        """
        Store an item in the cache.

        Args:
            key: The key to store the value under.
            value: The value to store in the cache.

        If either key or value is None, the method does nothing.
        """
        if key is None or value is None:
            return
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
