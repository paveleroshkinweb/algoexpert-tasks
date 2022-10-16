class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.buildHeap(array)

    def buildHeap(self, array):
        for el in array:
            self.insert(el)
        return self.heap

    def siftDown(self):
        if len(self.heap) > 1:
            index = 0
            child1, child2 = self.children_value(index)
            while child1 is not None:
                if child2 is None:
                    if self.heap[index] > child1:
                        self.swap(index, self.child1(index))
                    break
                m = min(self.heap[index], child1, child2)
                if m == self.heap[index]:
                    break
                if m == child1:
                    child_index = self.child1(index)
                else:
                    child_index = self.child2(index)
                self.swap(index, child_index)
                index = child_index
                child1, child2 = self.children_value(index)
                

    def siftUp(self):
        # Write your code here.
        if len(self.heap) > 1:
            index = len(self.heap) - 1
            parent_index = self.parent_index(index)
            while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = self.parent_index(index)

    def peek(self):
        return self.heap[0]

    def remove(self):
        if len(self.heap) == 0:
            return
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.siftDown()
        return result

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()

    def parent_index(self, index):
        return (index - 1) // 2

    def children(self, index):
        return self.child1(index), self.child2(index)

    def children_value(self, index):
        child1, child2 = self.children(index)
        return self.get_or_none(child1), self.get_or_none(child2)

    def child1(self, index):
        return 2 * index + 1

    def child2(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_or_none(self, index):
        if index < len(self.heap):
            return self.heap[index]
	
