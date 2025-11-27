import secrets
import string
from typing import List

def gen_pass(
    length: int = 12,
    include_lower: bool = True,
    include_upper: bool = True,
    include_special:bool = True,
    include_digits:bool = True,
    include_all: bool = True

) -> str:
    
    pools: List[str] = []

    if include_lower:
        pools.append(string.ascii_lowercase)
    if include_upper:
        pools.append(string.ascii_uppercase)
    if include_special:
        pools.append(string.punctuation)
    if include_digits:
        pools.append(string.digits)
    
    if not pools:
        raise ValueError("Atleastone type variable must be added")

    
    allchars = ''.join(pools)

    if include_all:
        if length < len(pools):
            raise ValueError(
                f"Password length must be >= {len(pools)} "
                f"to include one from each category."
            )
        password_char = [secrets.choice(pool) for pool in pools]
    