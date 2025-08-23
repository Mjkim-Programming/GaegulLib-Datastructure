class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self, data=None):
        self.length = 1 if data else 0
        self.head = LinkedNode(data) if data else None
        self.tail = self.head
            
    def __len__(self):
        return self.length
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return "<->".join(str(x) for x in self)
    
    def append(self, data):
        node = LinkedNode(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def appendleft(self, data):
        node = LinkedNode(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        
    def popleft(self):
        if not self.head:
            raise IndexError("pop from empty list")
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return data
    
    def pop(self):
        if not self.tail:
            raise IndexError("pop from empty list")
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return data
