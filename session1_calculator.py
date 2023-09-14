#Main Menu
print("Calculator.")
input("Press Enter to Start")

#Inputting two numbers
num1 = float(input("Enter Number 1 here>> "))
num2 = float(input("Enter Number 2 here>> "))

#Picking arithmetic operation
print("Enter any of the following numbers to decide which operation to use:"
    "\n1. Addition"
    "\n2. Subtraction"
    "\n3. Multiplication"
    "\n4. Division"
)
operation = int(input("Choose your operation >> "))

#Calculation process
if operation == 1:       #addition
    function = "adding"
    total = num1 + num2
elif operation == 2:     #subtraction
    function = "subtracting"
    total = num1 - num2
elif operation == 3:     #multiplication
    function = "multiplying"
    total = num1 * num2
elif operation == 4:     #division
    function = "dividing"
    total = num1 // num2
    total_float = num1 / num2
elif operation > 4 or operation < 5:
    total = 0
    print("You're either stupid or dropped as a baby.")

#Checks whether output is int or float
def is_integer(total):
    if isinstance(total, int):
        return True
    if isinstance(total, float):
        return total.is_integer()
    return False
if is_integer(total):
    total = int(total)
else:
    total = float(total)

if operation < 4:
    print(f"The result of {function} {num1} and {num2} is {total}. ")
elif operation == 4 and total == total_float: #If the result is a whole number, show answer as a integer.
    print(f"The result of {function} {num1} and {num2} is {total}.")
elif operation == 4 and total != total_float: #If the result is a decimal, show answer as a decimal.
    print(f"The result of {function} {num1} and {num2} is {total_float}")
elif operation > 4 or operation < 1:
    print("")