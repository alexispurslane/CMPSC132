#Lab #7
#Due Date: 04/24/2020, 11:59PM
########################################
#
# Name: Christopher Dumas
# Collaboration Statement:
#
########################################

class MaxPriorityQueue:
    '''
        >>> h = MaxPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
        >>> x = MaxPriorityQueue()
        >>> x.insert(2)
        >>> x.insert(7)
        >>> x.deleteMax()
        7
        >>> x.insert(10)
        >>> x.insert(8)
        >>> x.insert(12)
        >>> x.deleteMax()
        12
        >>> x.insert(5)
        >>> x.insert(18)
        >>> x.heap
        [18, 10, 8, 2, 5]
    '''

    def __init__(self):
        self.heap = []

    def __str__(self):
        return f'{self.heap}'

    __repr__ = __str__

    def __len__(self):
        return len(self.heap)

    def parent(self, index):
        lookup = index // 2 - 1
        if 0 <= lookup < len(self):
            return self.heap[lookup]
        else:
            return None

    def leftChild(self, index):
        lookup = 2 * index - 1
        if 0 <= lookup < len(self):
            return self.heap[lookup]
        else:
            return None

    def rightChild(self, index):
        lookup = 2 * index
        if 0 <= lookup < len(self):
            return self.heap[lookup]
        else:
            return None

    def __insert_raw(self, x):
        self.heap.append(x)
        return len(self.heap)

    def __bubbleUp(self, i):
        while self.parent(i) is not None and self.heap[i - 1] > self.parent(i):
            tmp = self.parent(i)
            self.heap[i // 2 - 1] = self.heap[i - 1]
            self.heap[i - 1] = tmp
            i = i // 2

    def insert(self, x):
        if len(self) == 0:
            self.heap = [x]
            return
        self.__bubbleUp(self.__insert_raw(x))

    def __bubbleDown(self, i):
        def assignLeft(i):
            tmp = self.heap[2 * i - 1]
            self.heap[2 * i - 1] = self.heap[i - 1]
            self.heap[i - 1] = tmp
            return 2 * i

        def assignRight(i):
            tmp = self.heap[2 * i]
            self.heap[2 * i] = self.heap[i - 1]
            self.heap[i - 1] = tmp
            return 2 * i + 1

        def testLeft(i):
            return self.leftChild(i) is not None and self.leftChild(i) > self.heap[i - 1]

        def testRight(i):
            return self.rightChild(i) is not None and self.rightChild(i) > self.heap[i - 1]

        while testLeft(i) or testRight(i):
            if testLeft(i) and testRight(i):
                if self.rightChild(i) < self.leftChild(i):
                    i = assignLeft(i)
                else:
                    i = assignRight(i)
            elif testLeft(i):
                i = assignLeft(i)
            elif testRight(i):
                i = assignRight(i)

    def deleteMax(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            outMax = self.heap[0]
            self.heap = []
            return outMax
        outMax = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.__bubbleDown(1)
        return outMax
