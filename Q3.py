#3. Python has a built-in function ‘map’ that applies a function to each element of a list.
#Provide an implementation for map using list comprehensions.

def new(number):
    return number + 2
numbers = [1, 2, 3, 4, 5]
updatedno = map(new, numbers)
print(list(updatedno))
