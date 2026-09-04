# Advanced Password Strength Checker

A multi-layered Python security tool that evaluates password strength beyond standard character-length checks.

## Features
- **Entropy Calculation:** Uses Shannon Entropy bits ($L \times \log_2(R)$) to evaluate true unpredictability.
- **Pattern & Walk Detection:** Identifies repeated characters (`aaa`), sequences (`123`, `abc`), and keyboard walks (`qwerty`).
- **Dictionary Lookups:** Identifies common default and frequently used weak passwords.
- **Breach Verification:** Integrates with the HaveIBeenPwned API using SHA-1 $k$-Anonymity to verify if passwords exist in real-world leaks without exposing the password.
- **Actionable Guidance:** Provides clear, practical feedback on how to fix detected security flaws.

## Project Structure
- `entropy.py`: Calculates character pool coverage and bit entropy.
- `patterns.py`: Detects sequences, repeated characters, and keyboard patterns.
- `dictionary.py`: Scans against frequent weak-password dictionaries.
- `breach.py`: Communicates with the HaveIBeenPwned API using privacy-preserving $k$-anonymity.
- `scorer.py`: Aggregates metrics into a 0–100 score and compiles feedback.
- `main.py`: Interactive CLI interface with masked input.

## How to Run
1. Install requirements:
   ```bash
   pip3 install requests