# Build a calculator from EC-Council course and add more features

import re
import math

print( "="*50 )
print("             MAGICAL CALCULATOR")
print("="*50)
print("Type 'quit' to exit, 'clear' to reset, 'history' to view past results\n")

previous = 0
history = []
run = True

def performMath():
    global run, previous, history

    prompt = f"[{previous}] → " if previous != 0 else "→ "
    equation = input(prompt)

    # Commands
    if equation.lower() == 'quit':
        print("\nThank you for using Magical Calculator. Goodbye! 👋")
        run = False
        return
    elif equation.lower() == 'clear':
        previous = 0
        print("Calculator reset!\n")
        return
    elif equation.lower() == 'history':
        print("\n=== Calculation History ===")
        if history:
            for i, value in enumerate(history, 1):
                print(f"{i}: {value}")
        else:
            print("No calculations yet.")
        print("===========================\n")
        return

    # Clean input
    equation = re.sub(r'[a-zA-Z,:?!{}@#%^&=|<>~]', '', equation).strip()

    # Map math functions
    equation = equation.replace("sqrt", "math.sqrt")
    equation = equation.replace("sin", "math.sin")
    equation = equation.replace("cos", "math.cos")
    equation = equation.replace("tan", "math.tan")
    equation = equation.replace("log", "math.log")
    equation = equation.replace("pow", "math.pow")

    try:
        # Fix for continuous calculation
        if previous != 0 and equation[0] in "+-*/":
            equation = f"{previous}{equation}"

        previous = eval(equation)
        print(f"Result: {previous}\n")
        history.append(previous)

    except Exception as e:
        print("Invalid input! Please enter a valid math expression.\n")

while run:
    performMath()
