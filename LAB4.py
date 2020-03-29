#Lab #4
#Due Date: 03/06/2020, 11:59PM
########################################
#
# Name: Christopher Dumas
# Collaboration Statement:
#
########################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class SortedLinkedList:
    '''
        >>> x = SortedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.pop()
        8.76
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 1 1 1 3 4 4 5 9.78
        >>> x=SortedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> x.add(58)
        >>> x.add(33)
        >>> x.add(1)
        >>> x.add(-88)
        >>> print(x)
        Head:Node(-88)
        Tail:Node(58)
        List:-88 -6 1 3 7 8.76 33 58
        >>> x.pop()
        58
        >>> print(x)
        Head:Node(-88)
        Tail:Node(33)
        List:-88 -6 1 3 7 8.76 33
        >>> x.pop()
        33
        >>> x.pop()
        8.76
        >>> x.pop()
        7
        >>> print(x)
        Head:Node(-88)
        Tail:Node(3)
        List:-88 -6 1 3
        >>> x.add(-4)
        >>> x.add(-4)
        >>> x.add(2)
        >>> x.add(2)
        >>> x.add(3)
        >>> print(x)
        Head:Node(-88)
        Tail:Node(3)
        List:-88 -6 -4 -4 1 2 2 3 3
        >>> x.add(65)
        >>> x.add(-100)
        >>> x
        Head:Node(-100)
        Tail:Node(65)
        List:-100 -88 -6 -4 -4 1 2 2 3 3 65
        >>> x=SortedLinkedList()
        >>> x.add(4)
        >>> x.replicate()
        Head:Node(4)
        Tail:Node(4)
        List:4 4 4 4
        >>> x.add(-23)
        >>> x.add(2)
        >>> x.add(1)
        >>> x.add(20.8)
        >>> x
        Head:Node(-23)
        Tail:Node(20.8)
        List:-23 1 2 4 20.8
        >>> x.replicate()
        Head:Node(-23)
        Tail:Node(20.8)
        List:-23 1 2 2 4 4 4 4 20.8
        >>> x.add(-1)
        >>> x.add(0)
        >>> x.add(3)
        >>> x.replicate()
        Head:Node(-23)
        Tail:Node(20.8)
        List:-23 -1 0 1 2 2 3 3 3 4 4 4 4 20.8
        >>> x
        Head:Node(-23)
        Tail:Node(20.8)
        List:-23 -1 0 1 2 3 4 20.8
        >>> x.add(2)
        >>> x.replicate()
        Head:Node(-23)
        Tail:Node(20.8)
        List:-23 -1 0 1 2 2 2 2 3 3 3 4 4 4 4 20.8
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):   # You are not allowed to modify this method
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__ = __str__

    def isEmpty(self):
        return self.head == self.tail

    def __len__(self):
        l = 0
        pointer = self.head
        while pointer is not None:
            pointer = pointer.next
            l += 1
        return l

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        elif value <= self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None and pointer.next.value < value:
                pointer = pointer.next

            tmp = pointer.next
            pointer.next = Node(value)
            pointer.next.next = tmp

            if tmp is None:
                self.tail = pointer.next

    def pop(self):
        if self.head is None:
            return None
        elif self.tail == self.head:
            tmp = self.head
            self.tail = self.head = None
            return tmp.value

        pointer = self.head
        while pointer.next.next is not None:
            pointer = pointer.next

        self.tail = pointer
        node = self.tail.next
        self.tail.next = None

        return node.value

    def replicate(self):
        x = SortedLinkedList()
        pointer = self.head
        while pointer is not None:
            if isinstance(pointer.value, int) and pointer.value > 0:
                for v in range(0, pointer.value):
                    x.add(pointer.value)
            else:
                x.add(pointer.value)
            pointer = pointer.next
        return x
