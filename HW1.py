#HW #1
#Due Date: 01/31/2020, 11:59PM 
########################################
#                                      
# Name: Christopher Dumas
# Collaboration Statement:             
#
########################################

import math

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10) # From a 2x5 rectangle
        5
        >>> rectangle(12, 5) # From a 1x5 rectangle
        5
        >>> rectangle(25, 25) # A 2.5x10, but one side is not an integer
        >>> rectangle(50, 100) # From a 5x20 rectangle
        20
        >>> rectangle(11, 5)
        >>> rectangle(11, 4)
    """
    side_total = perimeter / 2
    if round(side_total) != side_total:
        return None
    else:
        side_total = round(side_total)
    for x in range(1, side_total):
        for y in range(1, side_total - x + 1):
            if x*y == area and x + y == side_total:
                return max(x, y)
    return None

def translate(translation, txt):
    """
        >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
        >>> text = '1 UP, 2 down / left right forward' 
        >>> translate(myDict, text)
        '2 down 2 up right left forward'
        >>> text
        '1 UP, 2 down / left right forward'
        >>> translate({'a':'b'}, text)
        '1 up 2 down left right forward'
    """
    txt = txt.lower()
    txt = "".join([c for c in txt if c.isalnum() or c == ' '])
    newtxt = [translation[word] if word in translation else word for word in
              txt.split(" ")]
    return " ".join([word for word in newtxt if word != ''])

def onlyTwo(x, y, z):
    """
        >>> onlyTwo(1, 2, 3)
        13
        >>> onlyTwo(3, 3, 2)
        18
        >>> onlyTwo(5, 5, 5)
        50
    """
    if x < 0 or y < 0 or z < 0:
        return None

    numbers = [x, y, z]
    one = max(numbers)
    numbers.remove(one)
    two = max(numbers)

    return one**2 + two**2

def sumDigits(n):
    """
        >>> sumDigits(1001)
        2
        >>> sumDigits(59872)
        31

    """
    return sum(map(int, str(n)))

def largeFactor(n):
    """
        >>> largeFactor(15) # factors are 1, 3, 5
        5
        >>> largeFactor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
        40
        >>> largeFactor(13) # factor is 1 since 13 is prime
        1
    """
    candidates = [x for x in range(1, n) if n % x == 0]
    return candidates[-1]


def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(3.5)
        >>> hailstone(0)
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    if n <= 0 or not isinstance(n, int):
        return None
    lst = [n]
    while lst[-1] != 1:
        if lst[-1] % 2 == 0:
            lst.append(lst[-1] // 2)
        else:
            lst.append(3*lst[-1] + 1)
    # I want to make this a generator! (:
    return lst
