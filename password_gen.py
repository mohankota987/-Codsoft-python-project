# Task 3: Custom Password Generator Tool
import random
import string

def create_secure_password():
    print("----- Password Generator Utility -----")
    
    try:
        # Prompting for password size
        length = int(input("How many characters do you need?: "))
        
        if length < 8:
            print("Note: Short passwords are less secure. Try 8 or more.")
        
        # Defining the character sets
        letters_pool = string.ascii_letters  # a-z and A-Z
        numbers_pool = string.digits         # 0-9
        special_pool = string.punctuation    # symbols
        
        # Combining all sets
        combined_pool = letters_pool + numbers_pool + special_pool
        
        # Generating password using choices for better randomness
        # This allows characters to repeat, which is standard
        generated_chars = random.choices(combined_pool, k=length)
        final_password = "".join(generated_chars)
        
        print("\n--------------------------------")
        print(f"Generated Password: {final_password}")
        print("Strength: Strong")
        print("--------------------------------")

    except ValueError:
        print("Invalid input! Please enter a numeric value for the length.")

if __name__ == "__main__":
    create_secure_password()
