#2. Write a program wrap.py that takes filename and number of characters per line (width)
#as arguments. The program must wrap the lines of the file longer than entered width.

# sourcery skip: ensure-file-closed
import textwrap

value = """Write a program wrap.py that takes filename and number of characters per line (width)
as arguments. The program must wrap the lines of the file longer than entered width.
3. Python has a built-in function ‘map’ that applies a function to each element of a list.
Provide an implementation for map using list comprehensions."""

wrapper = textwrap.TextWrapper(width = 12)

word_list = wrapper.wrap(text=value)

# Print each line.
for element in word_list:
	print(element)
