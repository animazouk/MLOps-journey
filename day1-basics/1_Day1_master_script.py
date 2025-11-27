# ================================================
# DAY 1: PYTHON BASICS - MASTER SCRIPT
# Author: Adarsh Vishwakarma (@adarsh4553)
# Date: November 12, 2025
# Repo: github.com/animazouk/MLOps-journey
# Goal: Master print, strings, numbers, input
# ================================================

print("\n" + "="*60)
print(" DAY 1: PYTHON BASICS - MASTER SCRIPT ")
print(" Author: Adarsh Vishwakarma (@adarsh4553) ")
print(" Date: November 12, 2025 ")
print("="*60 + "\n")

# ------------------------------------------------
# 1. PRINT FUNCTION & ESCAPE SEQUENCES
# ------------------------------------------------
print("1. PRINT FUNCTION & ESCAPE SEQUENCES")
print("   /|")
print("  / |")
print(" /  |")
print("/___|\n")

# ------------------------------------------------
# 2. WORKING WITH STRINGS
# ------------------------------------------------
print("2. WORKING WITH STRINGS")
phrase = "Adarsh Vishwakarma"
print(f"Original: {phrase}")
print(f"Lowercase: {phrase.lower()}")
print(f"Length: {len(phrase)} characters (including space)")
print(f"Index of 'A': {phrase.index('A')}")
print(f"Replace: {phrase.replace('Adarsh', 'Adhya')}\n")

# ------------------------------------------------
# 3. WORKING WITH NUMBERS
# ------------------------------------------------
print("3. WORKING WITH NUMBERS")
print(f"Negative number: -2.453")
print(f"Positive number: 2.487")
print(f"BODMAS: 3 * 5 - 3 + (4 - 2) = {3 * 5 - 3 + (4 - 2)}")

my_num = 5
print(f"Concatenation: {str(my_num)} is my favorite number")

print(f"Absolute value: abs(-5.5) = {abs(-5.5)}")
print(f"Power: pow(3,2) = {pow(3,2)}")
print(f"Max: max([1,2,3,4,5,6,7,8,7,6,98]) = {max([1,2,3,4,5,6,7,8,7,6,98])}")

from math import *
print(f"Floor: floor(3.7) = {floor(3.7)}")
print(f"Ceil: ceil(3.2) = {ceil(3.2)}")
print(f"Square root: round(sqrt(4)) = {round(sqrt(4))}\n")

# ------------------------------------------------
# 4. GETTING INPUT FROM USER
# ------------------------------------------------
print("4. GETTING INPUT FROM USER")
name = input("Enter your name: ").strip()
print(f"Hi {name}! Welcome to MLOps Journey!\n")

# ------------------------------------------------
# 5. MINI PROJECT: PERSONALIZED GREETING
# ------------------------------------------------
print("5. MINI PROJECT: PERSONALIZED GREETING")
time = "11:30 PM IST"
date = "November 12, 2025"

print("="*50)
print(f"  HELLO {name.upper()}!  ")
print(f"  Time: {time}")
print(f"  Date: {date}")
print("  Day 1/65: Python Basics - MASTERED")
print("  2.5 hrs/day → Job-ready in 3 months")
print("="*50)