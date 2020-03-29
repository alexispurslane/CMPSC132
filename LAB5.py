#Lab #5
#Due Date: 03/22/2020, 11:59PM
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


class Queue:
    '''
        >>> x = Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.enqueue(4)
        >>> print(x)
        Head:Node(1)
        Tail:Node(4)
        Queue:1 2 3 4
        >>> x.isEmpty()
        False
        >>> len(x)
        4
        >>> x.dequeue()
        1
        >>> x.dequeue()
        2
        >>> x.dequeue()
        3
        >>> x.dequeue()
        4
        >>> x.dequeue()
        >>> print(x)
        Head:None
        Tail:None
        Queue:
        >>> x.enqueue(3)
        >>> x.enqueue(2)
        >>> print(x)
        Head:Node(3)
        Tail:Node(2)
        Queue:3 2
        >>> x.dequeue()
        3
        >>> print(x)
        Head:Node(2)
        Tail:Node(2)
        Queue:2
        >>> x.dequeue()
        2
        >>> print(x)
        Head:None
        Tail:None
        Queue:
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__ = __str__

    def isEmpty(self):
        return self.head is None and self.tail is None

    def enqueue(self, value):
        if self.tail is None:
            self.tail = Node(value)
        if self.tail:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        if self.isEmpty():
            return None
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node.value

    def __len__(self):
        i = 0
        second_to_tail = self.head
        while second_to_tail is not None:
            second_to_tail = second_to_tail.next
            i += 1
        return i
