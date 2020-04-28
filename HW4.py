#HW4
#Due Date: 04/25/2020, 11:59PM EST
########################################
#
# Name: Christopher Dumas
# Collaboration Statement:
#
########################################

class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class CacheList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))

    __repr__=__str__

    def __len__(self):
        return self.numItems

    def put(self, content, evictionPolicy):
        # Error cases
        if content.size > self.maxSize:
            return "Insertion not allowed. Content size is too large."
        elif self.find(content.cid) is not None:
            return f"Insertion of content item {content.cid} not allowed. Content already in cache."
        while self.remainingSize < content.size:
            if evictionPolicy == "mru":
                self.mruEvict()
            elif evictionPolicy == "lru":
                self.lruEvict()

        # Main Logic: add node as head, add tail if necessary
        self.remainingSize -= content.size
        self.numItems += 1

        n = Node(content)
        n.next = self.head
        self.head = n
        if self.head.next is None:
            self.tail = self.head

    def find(self, cid):
        # Error condition
        if len(self) == 0:
            return None
        prev_ptr = None
        pointer = self.head
        while pointer.value.cid != cid and pointer.next is not None:
            prev_ptr = pointer
            pointer = pointer.next
        if pointer.value.cid == cid:
            if self.head != pointer:
                if prev_ptr:
                    prev_ptr.next = pointer.next
                pointer.next = self.head
                self.head = pointer
            return self.head.value

    def update(self, cid, content):
        res = self.find(cid)
        if res is not None:
            self.head.value = content
            return self.head.value
        else:
            return None

    def mruEvict(self):
        if len(self) == 0:
            return
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.remainingSize += node.value.size
        self.numItems -= 1

    def lruEvict(self):
        if len(self) == 0:
            return
        elif len(self) == 1:
            node = self.head
            self.tail = self.head = None
            self.remainingSize += node.value.size
            self.numItems -= 1
            return
        prev_ptr = None
        pointer = self.head
        while pointer.next is not None:
            prev_ptr = pointer
            pointer = pointer.next
        if prev_ptr is not None:
            prev_ptr.next = None
        self.tail = prev_ptr
        self.remainingSize += pointer.value.size
        self.numItems -= 1

    def clear(self):
        self.remainingSize = self.maxSize
        self.head = None
        self.tail = None
        self.numItems = 0
        return 'Cleared cache!'


class Cache:
    """
    >>> cache = Cache()
    >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
    >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
    >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")

    >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
    >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
    >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")

    >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
    >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
    >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")

    >>> cache.insert(content1, 'lru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'lru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.insert(content3, 'lru')
    'Insertion not allowed. Content size is too large.'

    >>> cache.insert(content4, 'lru')
    'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
    >>> cache.insert(content5, 'lru')
    'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
    >>> cache.insert(content6, 'lru')
    'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'

    >>> cache.insert(content7, 'lru')
    "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
    >>> cache.insert(content8, 'lru')
    "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
    >>> cache.insert(content9, 'lru')
    "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:45
    ITEMS:1
    LIST:
    [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:16
    ITEMS:2
    LIST:
    [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
    [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.hierarchy[0].clear()
    'Cleared cache!'
    >>> cache.hierarchy[1].clear()
    'Cleared cache!'
    >>> cache.hierarchy[2].clear()
    'Cleared cache!'
    >>> cache
    L1 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:200
    ITEMS:0
    LIST:
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.insert(content1, 'mru')
    'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    >>> cache.insert(content2, 'mru')
    'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
    >>> cache.retrieveContent(content1)
    CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA
    >>> cache.retrieveContent(content2)
    CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD
    >>> cache.retrieveContent(content3)
    'Cache miss!'

    >>> cache.insert(content5, 'lru')
    'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
    >>> cache.insert(content6, 'lru')
    'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
    >>> cache.insert(content4, 'lru')
    'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'


    >>> cache.insert(content7, 'mru')
    "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
    >>> cache.insert(content8, 'mru')
    "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
    >>> cache.insert(content9, 'mru')
    "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
    >>> cache
    L1 CACHE:
    REMAINING SPACE:177
    ITEMS:2
    LIST:
    [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
    [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
    <BLANKLINE>
    <BLANKLINE>
    L2 CACHE:
    REMAINING SPACE:150
    ITEMS:1
    LIST:
    [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
    <BLANKLINE>
    <BLANKLINE>
    L3 CACHE:
    REMAINING SPACE:12
    ITEMS:2
    LIST:
    [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
    [CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>

    >>> cache.clear()
    'Cache cleared!'
    >>> contentA = ContentItem(2000, 52, "Content-Type: 2", "GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1")
    >>> contentB = ContentItem(2001, 76, "Content-Type: 2", "GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1")
    >>> contentC = ContentItem(2002, 11, "Content-Type: 2", "GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1")
    >>> cache.insert(contentA, 'lru')
    'INSERTED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1'
    >>> cache.insert(contentB, 'lru')
    'INSERTED: CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1'
    >>> cache.insert(contentC, 'lru')
    'INSERTED: CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1'
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentC)
    CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentA)
    CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> cache.retrieveContent(contentC)
    CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    >>> contentD = ContentItem(2002, 11, "Content-Type: 2", "GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1")
    >>> cache.insert(contentD, 'lru')
    'Insertion of content item 2002 not allowed. Content already in cache.'
    >>> contentE = ContentItem(2000, 52, "Content-Type: 2", "GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1")
    >>> cache.updateContent(contentE)
    'UPDATED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1'
    >>> cache.hierarchy[2]
    REMAINING SPACE:61
    ITEMS:3
    LIST:
    [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1]
    [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
    [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
    <BLANKLINE>
    <BLANKLINE>
    
    """

    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3

    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))

    __repr__=__str__

    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    def hashFunc(self, contentHeader):
        return sum(map(ord, list(contentHeader))) % self.size

    def insert(self, content, evictionPolicy):
        res = self.hierarchy[self.hashFunc(content.header)].put(content, evictionPolicy)
        return res or f'INSERTED: {content}'

    def retrieveContent(self, content):
        res = self.hierarchy[self.hashFunc(content.header)].find(content.cid)
        return res or 'Cache miss!'

    def updateContent(self, content):
        res = self.hierarchy[self.hashFunc(content.header)].update(content.cid, content)
        if res is not None:
            return f'UPDATED: {res}'
        else:
            return "Cache miss!"
