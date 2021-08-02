# İlk problem
from collections.abc import Iterable
 
def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def returnList(l):
    return list(flatten(l))

# print(returnList([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

def reverseList(l):
    l.reverse()
    for i in l:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            i.reverse()
    return l

# print(reverseList([[1, 2], [3, 4], [5, 6, 7]]))