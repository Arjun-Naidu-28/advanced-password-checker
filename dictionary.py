# dictionary.py
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "12345",
    "12345678", "welcome", "admin", "login", "iloveyou",
    "monkey", "dragon", "master", "sunshine", "princess"
]

def check_common_dictionary(password):
    """Checks if the password is or contains a common weak word."""
    clean_pwd = password.lower().strip()
    for word in COMMON_PASSWORDS:
        if word in clean_pwd:
            return True, word
    return False, None