def check_repeated_chars(password):
    """Returns True if any character repeats 3 times in a row (e.g., 'aaa')."""
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False

def check_sequences(password):
    """Returns True if characters follow an alphabetical/numerical run like 'abc' or '321'."""
    lower_pwd = password.lower()
    for i in range(len(lower_pwd) - 2):
        val1, val2, val3 = ord(lower_pwd[i]), ord(lower_pwd[i+1]), ord(lower_pwd[i+2])
        # Forward sequence (1-2-3 or a-b-c)
        if val2 == val1 + 1 and val3 == val2 + 1:
            return True
        # Backward sequence (3-2-1 or c-b-a)
        if val2 == val1 - 1 and val3 == val2 - 1:
            return True
    return False

def check_keyboard_walks(password):
    """Returns True if 3 characters walk across standard keyboard rows."""
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]
    lower_pwd = password.lower()
    
    for i in range(len(lower_pwd) - 2):
        chunk = lower_pwd[i:i+3]
        for row in rows:
            if chunk in row or chunk in row[::-1]:
                return True
    return False

def find_patterns(password):
    """Runs all checks and returns a list of detected issues."""
    found = []
    if check_repeated_chars(password):
        found.append("Repeated characters (e.g. 'aaa')")
    if check_sequences(password):
        found.append("Sequential characters (e.g. '123' or 'abc')")
    if check_keyboard_walks(password):
        found.append("Keyboard walk (e.g. 'qwer')")
    return found

if __name__ == "__main__":
    test_pwd = "Password123!"
    print(f"Testing password: {test_pwd}")
    print("Detected patterns:", find_patterns(test_pwd))