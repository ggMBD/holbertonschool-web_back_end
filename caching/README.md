# Caching

## Description
This project implements different caching systems in Python.
Each cache has a maximum size of 4 items (MAX_ITEMS = 4) and uses
a different eviction policy when the cache is full.

## Requirements
- Python 3.8+
- pycodestyle 2.7.x

## BaseCaching
All caching classes inherit from `BaseCaching` which provides:
- `self.cache_data` — dictionary to store cache items
- `MAX_ITEMS = 4` — maximum number of items in the cache

## Tasks

### Task 0 — BasicCache
No eviction policy. Items are stored indefinitely with no size limit.

### Task 1 — FIFO Cache
**First In First Out** — when the cache is full, the oldest inserted item is discarded.

### Task 2 — LIFO Cache
**Last In First Out** — when the cache is full, the most recently inserted item is discarded.

### Task 3 — LRU Cache
**Least Recently Used** — when the cache is full, the item that hasn't been accessed for the longest time is discarded.

### Task 4 — MRU Cache
**Most Recently Used** — when the cache is full, the most recently accessed item is discarded.

## Author
Maouia