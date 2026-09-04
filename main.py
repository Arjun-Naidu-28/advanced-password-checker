# main.py
from scorer import evaluate_password

def run_checker():
    print("\n" + "=" * 50)
    print("      ADVANCED PASSWORD STRENGTH CHECKER      ")
    print("=" * 50)
    
    # Regular input lets you see everything you type
    user_pwd = input("Enter password to test: ")

    if not user_pwd:
        print("Password cannot be empty.")
        return

    print("\nAnalyzing password against security benchmarks...")
    result = evaluate_password(user_pwd)

    print("\n" + "-" * 20 + " RESULTS " + "-" * 20)
    print(f"Overall Rating  : {result['rating']}")
    print(f"Total Score     : {result['score']} / 100")
    print(f"Shannon Entropy : {result['entropy']} bits")
    print(f"Breach Sightings: {result['breach_count']}")
    
    if result["feedback"]:
        print("\nActionable Recommendations:")
        for tip in result["feedback"]:
            print(f"  * {tip}")
    else:
        print("\nExcellent! Your password passes all security checks.")
    print("-" * 49 + "\n")

if __name__ == "__main__":
    run_checker()