# ================================================
# DAY 3: 2D LISTS, EXCEPTIONS, FILE I/O, MODULES
# Author: Adarsh Vishwakarma (@adarsh4553)
# Date: November 14, 2025
# Repo: github.com/adarsh4553/MLOPS-journey
# ================================================

print("\n" + "="*60)
print(" DAY 3: MY LEARNING FROM VIDEO ")
print("="*60 + "\n")

# ------------------------------------------------
# 1. 2D LISTS & NESTED LOOPS
# ------------------------------------------------
print("1. 2D LISTS")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(f"number_grid[1][2] = {number_grid[1][2]}")

print("Nested loop output:")
for row in number_grid:
    for element in row:
        print(element, end=" ")
    print()
print()

# ------------------------------------------------
# 2. EXCEPTION HANDLING
# ------------------------------------------------
print("2. EXCEPTION HANDLING")
try:
    value = 10 / 2
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
print()

# ------------------------------------------------
# 3. FILE HANDLING
# ------------------------------------------------
print("3. FILE HANDLING")
emp_file = open("employees.txt", "a+")
emp_file.seek(0)
print("File content:")
print(emp_file.read())
emp_file.write("\nThis is a test message\n")
print("Wrote: 'This is a test message'")
emp_file.close()
print()

# ------------------------------------------------
# 4. MODULES & PIP
# ------------------------------------------------
print("4. MODULES & PIP")
try:
    import translator
    phrase = input("Enter phrase: ")
    print(translator.translate(phrase))
except ImportError:
    print("translator module not found. Install with: pip install googletrans==4.0.0-rc1")
print()

# ------------------------------------------------
# 5. not {variable}
# ------------------------------------------------

'''
Python considers some values as False:
Value       Boolean Meaning  

0               False
""              False
None            False
[]              False
{}              False
()              False

'''
#Example:
grid = []

if not grid:
    print("empty grid")