#Lab #3
#Due Date: 02/21/2020, 11:59PM 
########################################
#
# Name: Christopher Dumas
# Collaboration Statement: 
#
########################################

import math

# I actually think in recursive functions and then convert into loops most of
# the time. That happens when your second (and most used) programming language
# is a Scheme.

def thirtyTwos(n):
    '''
        >>> thirtyTwos(432601)
        1
        >>> thirtyTwos(132432601)
        2
        >>> thirtyTwos(78)
        0
    '''
    if n == 0:
        return 0
    else:
        lastDigit = n % 10
        nextDigit = (n // 10) % 10
        if lastDigit == 2 and nextDigit == 3:
            return 1 + thirtyTwos(n // 10)
        else:
            return thirtyTwos(n // 10)


def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    if len(aList) == 0:
        return []
    else:
        if isinstance(aList[0], list):
            return flat(aList[0]) + flat(aList[1:])
        else:
            return [aList[0]] + flat(aList[1:])


def triangle(n):
    return recursiveTriangle(n, n)


def recursiveTriangle(k, n):
    '''
        >>> recursiveTriangle(2,4)
        '  **\\n   *'
        >>> print(recursiveTriangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    if k == 0:
        return ""
    else:
        newline = "\n"
        if k == 1:
            newline = ""
        return " " * (n - k) + "*" * k + newline + recursiveTriangle(k - 1, n)


def isPrime(num, i=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    if i > math.sqrt(num):
        return not (num == 1 or num == 0)
    else:
        return not (num % i == 0) and isPrime(num, i + 1)
