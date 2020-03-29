#Lab #1
#Due Date: 01/24/2020, 11:59PM 
########################################
#                                      
# Name: Christopher Dumas
# Collaboration Statement: One Man Army
#
########################################

import re
from collections import defaultdict

# NOTE: If you use input() for testing, don't forget to remove it before submitting

def common(list1, list2):
    """
        >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        [44, 12, 3, 1]
        >>> common([1,2,3],[4,5,6])
        []
    """
    # sets already have this functionality, let's just use these---it's bad code smell to reinvent stuff.
    return list(reversed(sorted(set(list1).intersection(set(list2))))) 

def connect(list1, list2, k):
    """
        >>> connect([1,2,3,4], [5,6], 2)
        [1, 2, 5, 6, 3, 4]
        >>> connect([1,2,3,4], [5,6,7,8,9,10], 3)
        [1, 2, 3, 5, 6, 7, 8, 9, 10, 4]
    """
    a = list1[:k]
    b = list1[k:]
    return a + list2 + b

def countWords(document):
    """
        >>> expected={'he': 4, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 2, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        >>> countWords('article.txt')==expected
        True
    """
    # Open the file and read the contents
    f = open(document,"r")

    if f.mode == 'r': # Verify that the file was opened
        contents = f.read() # use the read() function to read the entire file, contents has the data as string

    # Replace newlines with something more useful, and get rid of anything that
    # isn't alphabetic (or a space, we need those!)
    lines = re.sub(r'[^a-zA-Z ]', '', re.sub(r'\n|\r|\f', ' ', contents))
    words = defaultdict(int) # makes the logic a little nicer (: just gives a
                             # default value to any item in the dict
    for word in lines.split(' '):
        sanitized = word.lower().strip()
        if sanitized != '':
            words[sanitized] += 1
    return dict(words)
