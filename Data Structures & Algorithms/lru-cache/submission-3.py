class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cacheMap = {} # key: node
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, prev=None, val=0, nxt=None, key=-1):
            self.nxt = nxt
            self.val = val
            self.prev = prev
            self.key = key
        
    def get(self, key: int) -> int:
        if key not in self.cacheMap: return -1
        self._update(key)
        return self.cacheMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self._update(key)
            self.tail.val = value
            return
        
        # init new Node 
        newNode = self.Node(self.tail, value, None, key)
        self.cacheMap[key] = newNode

        # full; del LRU, add new to MRU
        if self.count == self.capacity:
            # delete LRU elem, add new to end 
            del self.cacheMap[self.head.key]
            self.head = self.head.nxt
            if not self.head: # capacity = 1 case
                self.head, self.tail = newNode, newNode
                newNode.prev = None
            else:
                self.head.prev = None
                self.tail.nxt = newNode
                self.tail = newNode
                
        # not full, init if empty, otherwise add to end
        else:
            # empty
            if not self.head:
                self.head, self.tail = newNode, newNode
            else:
                self.tail.nxt = newNode
                self.tail = newNode
            self.count += 1

    def _update(self, key):
        # fetch node
        curr = self.cacheMap[key]
        # remove and add to back
        if curr is self.head: # remove from front
            self.head = self.head.nxt
            if not self.head: # list now empty
                self.head, self.tail = curr, curr
            else:
                self.head.prev = None
                self.tail.nxt = curr
                curr.prev = self.tail
                curr.nxt = None
                self.tail = curr
        
        # simply leave it alone
        elif curr is self.tail:
            return
        
        # relink curr.prev/curr.next, add to back and relink
        else:
            # remove curr
            curr.prev.nxt = curr.nxt
            curr.nxt.prev = curr.prev
            # add to back
            self.tail.nxt = curr
            curr.prev = self.tail
            curr.nxt = None
            self.tail = curr

        # finally lol
        return curr.val