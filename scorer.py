from entropy import check_basic_rules, calculate_entropy
from patterns import find_patterns
from dictionary import check_common_dictionary
from breach import check_breach_count

def evaluate_password(password):
    score = 0
    feedback = []

    # 1. Base rule checks (Up to 60 points)
    rules = check_basic_rules(password)
    
    if not rules["length"]:
        feedback.append(f"Make it longer: Currently {len(password)} characters (aim for 12+).")
    else:
        score += 20

    if not rules["has_upper"]:
        feedback.append("Add at least one uppercase letter (A-Z).")
    else:
        score += 10

    if not rules["has_lower"]:
        feedback.append("Add at least one lowercase letter (a-z).")
    else:
        score += 10

    if not rules["has_digit"]:
        feedback.append("Add at least one number (0-9).")
    else:
        score += 10

    if not rules["has_symbol"]:
        feedback.append("Add at least one special symbol (!@#$%^&*).")
    else:
        score += 10

    # 2. Entropy bonus (Up to 40 points)
    entropy = calculate_entropy(password)
    if entropy >= 60:
        score += 40
    elif entropy >= 36:
        score += 20
    else:
        score += 5
        feedback.append("Entropy is low: Mix in more random character types.")

    # 3. Pattern penalties (-15 points per pattern)
    detected_patterns = find_patterns(password)
    for p in detected_patterns:
        score -= 15
        feedback.append(f"Avoid pattern: Remove {p}.")

    # 4. Dictionary penalty (-30 points)
    in_dict, match = check_common_dictionary(password)
    if in_dict:
        score -= 30
        feedback.append(f"Avoid common words: Contains '{match}'.")

    # 5. Breach check (Automatic failure if leaked)
    breach_count = check_breach_count(password)
    if breach_count > 0:
        score = 0
        feedback.append(f"CRITICAL: Found in {breach_count:,} public breaches! Never use this.")

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    # Determine overall rating
    if score >= 80:
        rating = "Very Strong"
    elif score >= 60:
        rating = "Strong"
    elif score >= 40:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "score": score,
        "rating": rating,
        "entropy": entropy,
        "feedback": feedback,
        "breach_count": breach_count
    }

if __name__ == "__main__":
    test_pwd = "Password123!"
    result = evaluate_password(test_pwd)
    print("--- Test Evaluation ---")
    print("Rating:", result["rating"])
    print("Score:", result["score"], "/ 100")
    print("Entropy:", result["entropy"], "bits")
    print("Breaches:", result["breach_count"])
    print("Tips to fix:")
    for tip in result["feedback"]:
        print(" -", tip)