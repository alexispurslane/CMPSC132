
#Lab #0
#Due Date: 01/17/2020, 11:59PM
########################################
#
# Name: Christopher Dumas
# Collaboration Statement: No One
#
########################################


def sumSquares(aList):
    """
        >>> sumSquares(5)
        >>> sumSquares('5')
        >>> sumSquares(6.15)
        >>> sumSquares([1,5,-3,5,9,8,4])
        90
        >>> sumSquares(['3',5,-3,5,9.0,8,4,'Hello'])
        90.0
    """

    if not isinstance(aList, list):
        return None

    return sum(x*x for x in aList if isinstance(x, (int, float, complex))\
               and abs(x) % 3 == 0)
