import secrets
import string
from typing import Optional

def generate_password(length: int = 12,
                      upper: bool = True,
                      digits: bool = True,
                      special: bool = True,
                      require_each_category: bool = True) -> str:
    """
    Generate a secure random password.

    Args:
        length: total length of the password (must be >= 1).
        upper: include uppercase letters A-Z.
        digits: include digits 0-9.
        special: include punctuation characters.
        require_each_category: if True, ensure the password contains at least
                               one character from each enabled category.

    Returns:
        A securely generated password string.
    """
    #if password it too short it raises an error
    if length < 1:
        raise ValueError("length must be >= 1")

    pools = []#   created a list to contain all the valid values for each type
  
    lower_pool = string.ascii_lowercase#   A default type lower case characters
    pools.append(lower_pool)

#   if true will add thease as well
    if upper:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if special:
        pools.append(string.punctuation)

#   Combined pool
    all_chars = ''.join(pools)
    if not all_chars:
        raise ValueError("No characters available to generate password")

    if require_each_category:
        # Ensure there is at least one char from each enabled pool
        if length < len(pools):
            raise ValueError(
                f"length must be at least number of enabled categories ({len(pools)})"
            )
        # Start with one guaranteed char from each pool:
        password_chars = [secrets.choice(pool) for pool in pools]
        # Fill the rest randomly from the full pooled chars
        remaining = length - len(password_chars)
        password_chars += [secrets.choice(all_chars) for _ in range(remaining)]
        # Shuffle to remove predictable positions (use secrets-level shuffle via secrets.randbelow)
        # Python doesn't provide secrets.shuffle, so implement Fisher–Yates using secrets.randbelow:
        for i in range(len(password_chars) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password_chars[i], password_chars[j] = password_chars[j], password_chars[i]
        return ''.join(password_chars)
    else:
        # Simple generation without enforcing each category
        return ''.join(secrets.choice(all_chars) for _ in range(length))

# Example usage:
if __name__ == "__main__":
    print(generate_password(12, upper=True, digits=True, special=True))