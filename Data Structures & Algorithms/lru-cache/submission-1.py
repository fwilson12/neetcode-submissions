from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elems = 0
        self.cache = deque() # queue in which the front element is the LRU key
        self.cacheMap = {} # k: v


    def get(self, key: int) -> int:
        
        # refresh place in removal queue
        if key in self.cacheMap:
            self.cache.remove(key)
            self.cache.append(key)
            return self.cacheMap[key]
        else:
            return -1
        
         
        

    def put(self, key: int, value: int) -> None:
        
        # update existing element
        if key in self.cacheMap:
            # remove from queue and append right (it's recently used, so refresh it's place in the removal queue)
            self.cache.remove(key)
            self.cache.append(key)
            # update cacheMap
            self.cacheMap[key] = value
            return 
        
        # we're full, remove LRU key
        if self.elems == self.capacity:
            
            # remove LRU key from cacheMap, then pop from front
            del self.cacheMap[self.cache[0]]
            self.cache.popleft()
            self.elems -= 1

        # add new key to queue and cacheMap
        self.cache.append(key)
        self.cacheMap[key] = value
        self.elems += 1
