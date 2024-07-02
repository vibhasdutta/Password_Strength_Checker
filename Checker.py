import re
import math
from termcolor import colored

def banner():
    print(colored("=" * 40, 'blue'))
    print(colored(" " * 10 + "PASSWORD STRENGTH CHECKER", 'green'))
    print(colored("=" * 40, 'blue'))
    print()

def footer():
    print(colored("=" * 40, 'blue'))
    print(colored(" " * 12 + "CHECK COMPLETE", 'green'))
    print(colored("=" * 40, 'blue'))

def check_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    strength_score = sum(strength_criteria.values())
    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    # Calculate the number of possible combinations
    character_set_size = 0
    if strength_criteria["uppercase"]:
        character_set_size += 26
    if strength_criteria["lowercase"]:
        character_set_size += 26
    if strength_criteria["digits"]:
        character_set_size += 10
    if strength_criteria["special"]:
        character_set_size += 32  # Assuming 32 special characters
    
    # Brute force calculation: time to crack in seconds
    combinations = character_set_size ** len(password)
    attempts_per_second = 1e10  # Assume 10 billion attempts per second
    time_to_crack_seconds = combinations / attempts_per_second
    
    # Convert time to years
    seconds_per_year = 60 * 60 * 24 * 365.25
    time_to_crack_years = time_to_crack_seconds / seconds_per_year
    
    # Provide feedback
    feedback = f"Password strength: {strength[strength_score-1]}"
    feedback += f"\nEstimated time to crack: {time_to_crack_years:.2e} years"
    
    # Detailed feedback on missing criteria
    missing_criteria = [key for key, value in strength_criteria.items() if not value]
    if missing_criteria:
        feedback += "\nConsider adding the following to improve strength: " + ", ".join(missing_criteria)
    
    return feedback

def main():
    banner()
    password = input(colored("Enter a password to check its strength: ", 'yellow'))
    print()
    print(colored(check_password_strength(password), 'cyan'))
    print()
    footer()

if __name__ == "__main__":
    main()
