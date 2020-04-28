#LAB 9
#Due Date: 04/11/2020, 11:59PM EST
########################################
#
# Name: Christopher Dumas
# Collaboration Statement:
#
########################################

class MaxPriorityQueue:
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

def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sortHeap = MaxPriorityQueue()
    for x in numList:
        sortHeap.insert(x)
    result = []
    y = sortHeap.deleteMax()
    while y != None:
        result.insert(0, y)
        y = sortHeap.deleteMax()
    return result
