import hashlib
import requests

def check_breach_count(password):
    """
    Checks the HaveIBeenPwned API using k-Anonymity.
    Returns how many times this password has appeared in public data breaches.
    """
    # 1. Turn the password into an uppercase SHA-1 hash
    sha1_pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_pwd[:5]
    suffix = sha1_pwd[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        # 2. Ask the API for all hashes starting with the 5-character prefix
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return 0  # Server error or rate limited, fail safely
            
        # 3. Read through the returned lines (formatted like 'SUFFIX:COUNT')
        lines = response.text.splitlines()
        for line in lines:
            hash_suffix, count = line.split(':')
            if hash_suffix == suffix:
                return int(count)
                
        return 0  # Not found in any breach
    except requests.RequestException:
        # If your Mac is offline or has no connection
        return 0

if __name__ == "__main__":
    test_pwd = "password123"
    print(f"Checking '{test_pwd}' against leaked databases...")
    count = check_breach_count(test_pwd)
    print(f"Times seen in real data breaches: {count:,}")