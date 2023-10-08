from collections import deque

class LRUCache:
   def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = {}
      self.lru = deque()

   def put(self, key: int, value: int) -> None:
      if key in self.cache:
         self.cache[key] = value
         self.lru.remove(key)
         self.lru.append(key)
      else:
         if len(self.cache) == self.capacity:
               self.cache.pop(self.lru.popleft())
         self.cache[key] = value
         self.lru.append(key)

   def get(self, key: int) -> int:
      if key in self.cache:
         self.lru.remove(key)
         self.lru.append(key)
         return self.cache[key]
      else:
         return -1
        
if __name__ == '__main__':
   cache = LRUCache(2)
   cache.put(1, 1)
   cache.put(2, 2)
   print(cache.get(1))
   cache.put(3, 3)
   print(cache.get(2))
   cache.put(4, 4)
   print(cache.get(1))
   print(cache.get(3))
   print(cache.get(4))