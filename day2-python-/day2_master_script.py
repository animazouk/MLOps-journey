# ================================================
# DAY 2: LOOPS, LISTS, FUNCTIONS, DICTIONARIES
# Author: Adarsh Vishwakarma (@adarsh4553)
# Date: November 13, 2025
# Repo: github.com/adarsh4553/MLOPS-journey
# ================================================

print("\n" + "="*60)
print(" DAY 2: LOOPS, LISTS, FUNCTIONS, DICTIONARIES ")
print("="*60 + "\n")

# ------------------------------------------------
# 1. LISTS
# ------------------------------------------------
print("1. LISTS")
friends = ["adarsh", "divyansh", "Deepak"]
jobs = ["painter", "labour", "contractor"]
print(f"Friends: {friends}")
print(f"Jobs: {jobs}\n")

# Indexing & Slicing
print("Indexing & Slicing:")
print(f"First friend: {friends[0]}")
friends[1] = "Divyanshi"
print(f"Last friend: {friends[-1]}")
print(f"All from start: {friends[0:]}")
print(f"First two: {friends[0:2]}\n")

# List Functions
print("List Functions:")
friends.extend(jobs)
print(f"After extend(jobs): {friends}")

friends.append("ADHYA")
print(f"After append: {friends}")

friends.insert(2, "Luv")
print(f"After insert(2, 'Luv'): {friends}")

friends.remove("ADHYA")
print(f"After remove('ADHYA'): {friends}")

print(f"Index of 'Deepak': {friends.index('Deepak')}")

friends.append("adarsh")
print(f"Count of 'adarsh': {friends.count('adarsh')}")

friends.sort()
print(f"After sort(): {friends}")

friends.reverse()
print(f"After reverse(): {friends}")

f1 = friends.copy()
print(f"Copy: {f1}")

friends.pop()
print(f"After pop(): {friends}\n")

# ------------------------------------------------
# 2. TUPLES
# ------------------------------------------------
print("2. TUPLES")
coordinate = (4, 5)
print(f"Coordinate: {coordinate}")

coordinates = [(4,5), (6,4), (-3,6)]
print(f"First tuple: {coordinates[0]}")
print(f"Second value of first tuple: {coordinates[0][1]}\n")

# ------------------------------------------------
# 3. FUNCTIONS
# ------------------------------------------------
print("3. FUNCTIONS")
def sayhi(name):
    print(f"Hello {name}")

print("top")
sayhi("Adarsh")
print("bottom\n")

def cube(num):
    return num ** 3

result = cube(3)
print(f"Cube of 3: {result}\n")

# ------------------------------------------------
# 4. IF/ELIF/ELSE + NESTED
# ------------------------------------------------
print("4. CONTROL FLOW")
is_male = True
is_tall = True

if is_male or is_tall:
    if is_male and is_tall:
        print("Tall male")
    elif is_male and not is_tall:
        print("Male but not tall")
    else:
        print("Not male, probably not tall")
else:
    print("Not male and not tall")
print()

# ------------------------------------------------
# 5. COMPARISONS IN FUNCTION
# ------------------------------------------------
def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

print(f"Max of 1,2,3: {max_num(1,2,3)}\n")

# ------------------------------------------------
# 6. DICTIONARIES
# ------------------------------------------------
print("6. DICTIONARIES")
month_conversion = {
    "Jan": "January",
    "Feb": "February",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_conversion.get("Feb", "Not a valid key"))
print(month_conversion.get("XYZ", "Invalid month!"))  # Default used
print()

# ------------------------------------------------
# 7. WHILE LOOP
# ------------------------------------------------
print("7. WHILE LOOP")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# ------------------------------------------------
# 8. FOR LOOP
# ------------------------------------------------
print("8. FOR LOOP")
for letter in "Air Force School":
    print(letter, end="")
print("\n")

for friend in friends:
    print(friend)

print("Range 3 to 9:")
for x in range(3, 10):
    print(x, end=" ")
print("\n")

# ------------------------------------------------
# 9. EXPONENT FUNCTION
# ------------------------------------------------
print("9. EXPONENT FUNCTION")
def raise_to_power(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return result

print(f"2^3 = {raise_to_power(2, 3)}")

a = " add Buy Milk"
print(a)
print(a.strip())