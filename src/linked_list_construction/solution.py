class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)
            
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert
        
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        assert position >= 1
        current = self.head
        while current and position > 1:
            current = current.next
            position -= 1
        if current:
            self.insertBefore(current, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current:
            new_current = current.next
            if current.value == value:
                self.remove(current)
            current = new_current

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


    def containsNodeWithValue(self, value):
        # Write your code here.
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
