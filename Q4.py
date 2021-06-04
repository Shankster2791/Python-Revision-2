#Python has a built-in function ‘filter(f, a)’ that returns items of the list ‘a’ for which
#f(item) returns true. Provide an implementation for filter using list comprehensions


def startsWithJ(element):
    if len(element) > 0:
             return element[0] == 'J'
    return False
    
names = ('Jack', 'Jill', 'Steve', '')
ls=filter(startsWithJ, names)
print(list(ls))
