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
'''
# random and string
	•	random is Python’s standard pseudo-random number generator (PRNG) module. It is fast and fine for simulations, simple games, non-security use. Not recommended for cryptographic secrets (passwords, tokens).
	•	string is a helper module that defines useful string constants, such as:
	•	string.ascii_lowercase → 'abcdefghijklmnopqrstuvwxyz'
	•	string.ascii_uppercase → 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	•	string.digits → '0123456789'
	•	string.punctuation → common punctuation characters (varies, but includes e.g. !@#$%...)
	•	In production for secrets, prefer the secrets module (Python 3.6+) because it uses a cryptographically secure RNG.
    '''
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
print()

# ------------------------------------------------
# 6. secrets.choice(sequence)
# ------------------------------------------------
pool = "ajafbdsfkakasfb"
import secrets
char = secrets.choice(pool)  # What does this pick?
'''
#   The function:
pythonsecrets.choice(sequence)
Randomly returns one element from the given sequence.

sequence can be a list, tuple, or string.
It picks one item from it uniformly at random, using cryptographically secure randomness.
'''
print()


# ========================================================
# 7. SECURE PASSWORD GENERATOR (MASTER REUSABLE TEMPLATE)
# ========================================================
 
import secrets
import string
from typing import List

def generate_secure_password(
    length: int = 12,
    include_lower: bool = True,
    include_upper: bool = True,
    include_digits: bool = True,
    include_special: bool = True,
    require_one_from_each: bool = True,
    exclude_ambiguous: bool = True
) -> str:
    """
    Generate a cryptographically secure password with full policy control.

    Features:
    - Uses `secrets` module (not `random`) → OS-level secure RNG
    - Guarantees one char from each enabled category (if required)
    - Shuffles securely to avoid patterns
    - Optional: removes 0/O, 1/l, I/l, etc.

    Example:
        generate_secure_password(16, require_one_from_each=True)
        → 'G9@mPx!vQ2kR8#n'
    """
    # -------------------------------------------------------------------------
    # 1. Build character pools based on user flags
    # -------------------------------------------------------------------------
    pools: List[str] = []

    if include_lower:
        pools.append(string.ascii_lowercase)     # 'abcdefghijklmnopqrstuvwxyz'
    if include_upper:
        pools.append(string.ascii_uppercase)     # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_digits:
        pools.append(string.digits)              # '0123456789'
    if include_special:
        pools.append(string.punctuation)         # '!@#$%^&*...' etc.

    if not pools:
        raise ValueError("At least one character type must be enabled.")

    # -------------------------------------------------------------------------
    # 2. Combine all allowed characters into one big pool
    # -------------------------------------------------------------------------
    all_chars = ''.join(pools)  # e.g., 'abc...XYZ...123...!@#...'

    # -------------------------------------------------------------------------
    # 3. (Optional) Remove ambiguous characters: 0,O,1,l,I,|,`
    # -------------------------------------------------------------------------
    if exclude_ambiguous:
        ambiguous = {'0', 'O', 'o', '1', 'l', 'I', 'i', '|', '`'}
        all_chars = ''.join(c for c in all_chars if c not in ambiguous)
        # Rebuild pools without ambiguous chars
        pools = [
            ''.join(c for c in pool if c not in ambiguous)
            for pool in pools
        ]
        pools = [p for p in pools if p]  # Remove empty pools
        if not pools:
            raise ValueError("No valid characters left after excluding ambiguous ones.")

    # -------------------------------------------------------------------------
    # 4. Enforce "one from each category" if required
    # -------------------------------------------------------------------------
    if require_one_from_each:
        if length < len(pools):
            raise ValueError(
                f"Password length must be >= {len(pools)} "
                f"to include one from each category."
            )

        # Step A: Pick ONE secure char from EACH pool
        password_chars = [secrets.choice(pool) for pool in pools]
        # → e.g., ['k', 'G', '7', '!']

        # Step B: Fill remaining slots from full pool
        remaining = length - len(password_chars)
        password_chars += [secrets.choice(all_chars) for _ in range(remaining)]
        # → e.g., ['k','G','7','!','m','P','x','2','@','v','Q','9']

    else:
        # Simple: all chars from full pool
        password_chars = [secrets.choice(all_chars) for _ in range(length)]

    # -------------------------------------------------------------------------
    # 5. SECURE SHUFFLE — Remove predictable positions
    #    Option 1: Use SystemRandom().shuffle() ← RECOMMENDED
    # -------------------------------------------------------------------------
    secrets.SystemRandom().shuffle(password_chars)

    # -------------------------------------------------------------------------
    # 6. (Alternative) Manual Fisher–Yates shuffle using secrets.randbelow
    #    Uncomment below if you can't use SystemRandom for some reason
    # -------------------------------------------------------------------------
    # for i in range(len(password_chars) - 1, 0, -1):
    #     j = secrets.randbelow(i + 1)
    #     password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    # -------------------------------------------------------------------------
    # 7. Join and return final password
    # -------------------------------------------------------------------------
    return ''.join(password_chars)


# =============================================================================
# EXAMPLE USAGE (Uncomment to test)
# =============================================================================
if __name__ == "__main__":
    print("Strong 16-char password:", generate_secure_password(16))
    print("No special, 10-char:", generate_secure_password(10, include_special=False))
    print("Only digits+upper:", generate_secure_password(8, include_lower=False, include_special=False))
    print("Require each type:", generate_secure_password(12, require_one_from_each=True))
<<<<<<< HEAD:day3-functions-opps/1_Day3_master_script.py
=======

#--------------------------------------------------------------------------
# 7. *args and **kwargs
# -------------------------------------------------------------------------

# *args --->
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Adarsh", "Vishwakarma", "Ada")

# **kwargs --->

def print_address(**kwargs):
    for key, vakue in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "123 fake str",
              city = "Detroit",
              state = "MI",
              zip = "208010")
>>>>>>> 006c0dc (Day 4: OOP – classes, properties, static methods, BankAccount):day3-functions-modules_and_more/1_Day3_master_script.py
