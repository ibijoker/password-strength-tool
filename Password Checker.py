import string
from enum import Enum

# 1. Standardized Outputs
class PasswordStrength(Enum):
    WEAK = "Weak: Password is too short or simple."
    MEDIUM = "Medium: Good, but could use more variety."
    STRONG = "Strong: Excellent password!"

def evaluate_password(password: str) -> PasswordStrength:
    """
    Evaluates password strength using optimized Pythonic generator expressions.
    """
    if not isinstance(password, str):
        raise ValueError("Error: Password must be a valid string.")

    # Condition Checks
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    # Calculate score
    score = sum([length_ok, has_upper, has_lower, has_number, has_symbol])
    
    # Evaluate Result
    if score == 5:
        return PasswordStrength.STRONG
    elif score >= 3:
        return PasswordStrength.MEDIUM
    
    return PasswordStrength.WEAK

# --- Interactive User Loop ---
if __name__ == "__main__":
    print("--- Interactive Password Strength Checker ---")
    print("Type 'quit' or 'exit' at any time to stop the program.\n")
    
    # 2. Infinite loop to keep asking for input
    while True:
        # 3. Get input directly from the user
        user_input = input("Enter a password to check: ")
        
        # 4. Give the user a way to break out of the loop
        if user_input.lower() in ['quit', 'exit']:
            print("Exiting program. Stay secure!")
            break
            
        # Skip empty inputs
        if not user_input:
            print("Please enter at least one character.\n")
            continue
            
        # 5. Evaluate the input and print the result
        result = evaluate_password(user_input)
        print(f"Result: {result.value}\n")