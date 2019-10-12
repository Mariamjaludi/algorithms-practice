class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.currentSize = 0
        self.capacity = capacity
        self.linkedlist = DLL()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.linkedlist.setHeadTo(self.cache[key])
        return self.cache[key].val

    def put(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.capacity:
                self.evictLR()
            else:
                self.currentSize += 1
            self.cache[key] = DLLNode(key, value)
        else:
            self.cache[key].val = value
        self.linkedlist.setHeadTo(self.cache[key])

    def evictLR(self):
        keyToRem = self.linkedlist.tail.key
        self.linkedlist.removeTail()
        del self.cache[keyToRem]


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
