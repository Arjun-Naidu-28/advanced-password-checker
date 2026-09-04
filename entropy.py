import math
import string

def check_basic_rules(password):
    """Checks character types and returns a dictionary of flags."""
    return {
        "length": len(password) >= 8,
        "has_upper": any(ch in string.ascii_uppercase for ch in password),
        "has_lower": any(ch in string.ascii_lowercase for ch in password),
        "has_digit": any(ch in string.digits for ch in password),
        "has_symbol": any(ch in string.punctuation for ch in password),
    }

def get_pool_size(password):
    """Finds the character pool size (R)."""
    pool = 0
    rules = check_basic_rules(password)
    
    if rules["has_lower"]:
        pool += 26
    if rules["has_upper"]:
        pool += 26
    if rules["has_digit"]:
        pool += 10
    if rules["has_symbol"]:
        pool += 32
        
    return pool

def calculate_entropy(password):
    """Calculates entropy in bits: E = length * log2(pool)."""
    if not password:
        return 0.0
    
    pool = get_pool_size(password)
    if pool == 0:
        return 0.0
        
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

if __name__ == "__main__":
    test_pwd = "MySecret123!"
    print(f"Testing password: {test_pwd}")
    print(f"Entropy: {calculate_entropy(test_pwd)} bits")