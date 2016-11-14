class Node(object):
    def __init__(self,key=None,value=None,prev=None,next=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self.delNode(node)
            self.setHead(node)
            return node.value
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.delNode(node)
            self.setHead(node)
        else:
            if len(self.map) >= self.capacity:
                self.map.pop(self.tail.prev.key)
                self.delNode(self.tail.prev)
            node = Node(key,value)
            self.map[key] = node
            self.setHead(node)



    def setHead(self,node):
        if node.prev == self.head:
            return
        else:
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

    def delNode(self,node):
            node.prev.next = node.next
            node.next.prev = node.prev
            # should clear the point!
            node.prev = None
            node.next = None

cache = LRUCache(1)
cache.set(2,1)
print(cache.get(2))
cache.set(3,2)
# cache.set('2',20)
# # print(cache.get_lru())
# # print(cache.get_indexMap())
# cache.set('1',30)
# # print(cache.get_lru())
# # print(cache.get_indexMap())
# print(cache.get('1'))
# cache.set('3',30)
# print(cache.get('2'))
