#1. Write a program to count frequency of characters in a paragraph.
test_str = """Write a program wrap.py that takes filename and number of characters per line (width)
as arguments. The program must wrap the lines of the file longer than entered width.
3. Python has a built-in function ‘map’ that applies a function to each element of a list.
Provide an implementation for map using list comprehensions."""

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print ("Frequency of characteres in given text is :\n "	+ str(all_freq))
