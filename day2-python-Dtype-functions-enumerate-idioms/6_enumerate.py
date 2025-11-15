# Correct Formats and Use Cases of enumerate()
# Basic Syntax:

# python
enumerate(iterable, start=0)
# iterable: any iterable object like list, tuple, string, etc.

# start: optional, the index from which to start counting (default is 0).

# Common Usage Examples:

# Looping over a list with default start (0):

# python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:

'''
text
0 apple
1 banana
2 cherry
'''

# Starting index from 1 instead of 0:

# python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, 1):
    print(index, fruit)
# Output:
'''
text
1 apple
2 banana
3 cherry

'''

# Enumerating over a tuple:

# python
colors = ('red', 'green', 'blue')
for i, color in enumerate(colors):
    print(i, color)

# Enumerating a dictionary’s items:

# python
d = {'a': 10, 'b': 20, 'c': 30}
for i, (key, value) in enumerate(d.items()):
    print(i, key, value)

# Accessing the next element from an enumerate object manually:

# python
fruits = ['apple', 'banana']
enum_obj = enumerate(fruits)
print(next(enum_obj))  # Outputs (0, 'apple')
print(next(enum_obj))  # Outputs (1, 'banana')

# Nested enumeration (e.g., matrix rows and columns):

# python
matrix = [[1,2], [3,4]]
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f'matrix[{i}][{j}] = {val}')
'''

Common Mistakes with enumerate():

1. Forgetting to unpack the tuple that enumerate() returns:
    or item in enumerate(lst): prints tuples (index, value) 
    instead of directly unpacking to variables.

2. Misusing start argument: Giving a non-integer or negative 
    number might cause unintended results.

3. Using enumerate where index isn't needed: If you don't 
    need the index, just iterate over the iterable directly.

4. Modifying the iterable while enumerating it: Can lead to
     unexpected behaviors or errors.

5. Confusing enumerate() with range(len()): They can achieve
     similar results, but enumerate is more Pythonic and cleaner.

6. To summarize, enumerate() simplifies looping with 
    counters, providing clear and concise code. Always 
    unpack it to get index and element, and use the optional 
    start parameter when you want your index to start from a
    value other than 0.

'''