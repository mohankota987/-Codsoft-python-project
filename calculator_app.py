# Task 2: A simple calculator for basic math operations

# My Calculator Script for CodSoft Task 2

def my_calc():
    print("--- Basic Logic Calculator ---")
    
    try:
        # Taking inputs with slightly different wording
        x = float(input("Enter your first number: "))
        y = float(input("Enter your second number: "))
        
        print("\nAvailable Operations: +, -, *, /")
        action = input("Which action do you want to perform?: ")

        # Using a variable to store the result first
        output = 0

        if action == '+':
            output = x + y
            print(f"\nThe Sum is: {output}")
        
        elif action == '-':
            output = x - y
            print(f"\nThe Difference is: {output}")
            
        elif action == '*':
            output = x * y
            print(f"\nThe Product is: {output}")
            
        elif action == '/':
            if y != 0:
                output = x / y
                print(f"\nThe Quotient is: {output}")
            else:
                print("\nError! You can't divide by zero.")
        
        else:
            print("\nThat's not a valid math symbol!")

    except ValueError:
        print("\nPlease enter numeric values only.")

if __name__ == "__main__":
    my_calc()
