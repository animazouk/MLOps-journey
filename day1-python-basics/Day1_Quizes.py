# ================================================
# DAY 1 PYTHON BASICS QUIZ
# Author: Adarsh Vishwakarma (@adarsh4553)
# Date: November 12, 2025
# Repo: github.com/adarsh4553/MLOPS-journey
# ================================================

print("=" * 60)
print("        DAY 1: PYTHON BASICS QUIZ")
print("        Fill answers → Run → Auto-check!")
print("=" * 60 + "\n")

# ------------------------------------------------
# QUESTION 1: print() & Escape Sequences
# ------------------------------------------------
print("Q1: What will this print? (Predict output)")
print("=" * 40)

# YOUR ANSWER HERE (Uncomment and write expected lines)
# print("Hello\nWorld")
# print("Python\tRocks")

# === AUTO-CHECK Q1 ===
expected_q1 = "Hello\nWorld\nPython\tRocks\n"
user_q1 = """
Hello
World
Python  Rocks"""
# ----- WRITE YOUR PREDICTION BELOW -----
user_q1 = """
Hello
World
Python	Rocks
"""
# ---------------------------------------

if user_q1.strip() == expected_q1.strip():
    print("Q1: CORRECT!")
else:
    print("Q1: WRONG! Check newlines and tabs.\n")


# ------------------------------------------------
# QUESTION 2: String Methods
# ------------------------------------------------
print("\nQ2: Fix the code to print exact output")
print("=" * 40)

phrase = "Adarsh Vishwakarma"

# YOUR ANSWER HERE (Fix each line)
print(f"Original: " + phrase)
print(f"UPPER: " + phrase.upper())           # ← Fix
print(f"Length:" + str(len(phrase)))             # ← Fix
print(f"First 'a': index " + str(phrase.index('a')) ) # ← Fix

# === AUTO-CHECK Q2 ===
q2_output = []
q2_output.append(f"Original: {phrase}")
q2_output.append(f"UPPER: {phrase.upper()}")
q2_output.append(f"Length: {len(phrase)}")
q2_output.append(f"First 'a': index {phrase.index('a')}")

print("\n".join(q2_output))
print()


# ------------------------------------------------
# QUESTION 3: Numbers & Math Module
# ------------------------------------------------
print("Q3: Predict output of math functions")
print("=" * 40)

from math import *

# YOUR ANSWER HERE (Predict each print)
# print(pow())      
print(8)
# print(abs(-7.2))      
print(7.2)
# print(max(10, 20, 5)) 
print(20)
# print(floor(4.9))     
print(4)
# print(ceil(4.1))      # ← ?
print(5)

# === AUTO-CHECK Q3 ===
print("Running math functions...")
print(pow(2, 3))
print(abs(-7.2))
print(max(10, 20, 5))
print(floor(4.9))
print(ceil(4.1))
print()


# ------------------------------------------------
# QUESTION 4: Type Conversion Error
# ------------------------------------------------
print("Q4: Fix the TypeError")
print("=" * 40)

age = 25
# print("I am " + age + " years old")  # ← ERROR!

# YOUR ANSWER HERE (Fix it)
print("I am " + str(age) + " years old")  # ← Fixed
print()


# ------------------------------------------------
# QUESTION 5: Interactive Input + f-string + Logic
# ------------------------------------------------
print("Q5: Write interactive program")
print("=" * 40)

# YOUR ANSWER HERE
name = input("Enter your name: ").strip()
num = int(input("Enter your favorite number: "))

print(f"Hi " + name + "! Your favorite number " + str(num) + " is ", end="")
if num % 2 == 0:
    print("even!")
else:
    print("odd!")
print()


# ================================================
# SOLUTIONS & EXPLANATIONS (DO NOT PEEK UNTIL DONE)
# ================================================
print("\n" + "=" * 60)
print(" SOLUTIONS & EXPLANATIONS")
print("=" * 60 + "\n")

print("Q1: Expected Output")
print("Hello")
print("World")
print("Python\tRocks")
print("- \\n = newline, \\t = tab\n")

print("Q2: String Methods")
print("Original: Adarsh Vishwakarma")
print("UPPER: ADARSH VISHWAKARMA")
print("Length: 18")
print("First 'a': index 3")
print("- .upper() → all caps")
print("- len() → counts spaces")
print("- .index('a') → first match\n")

print("Q3: Math Functions")
print("8")
print("7.2")
print("20")
print("4")
print("5")
print("- pow(base, exp)")
print("- abs() → positive")
print("- floor() → down, ceil() → up\n")

print("Q4: TypeError Fix")
print("I am 25 years old")
print("- Can't concat int + str → use str(age)\n")

print("Q5: Interactive Logic")
print("Hi Adarsh! Your favorite number 7 is odd!")
print("- input() → str, int() → convert")
print("- % 2 == 0 → even check\n")

print("=" * 60)
print(" QUIZ COMPLETE! COMMIT & PUSH NOW!")
print("=" * 60)