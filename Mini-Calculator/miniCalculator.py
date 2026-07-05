# calculator => addition , subtraction , multiplication , division
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def multiply(a,b):
    return a * b

calculator = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division'
 }
for key, value in calculator.items():
    print(f"{key}: {value}")


user_input = input("Select operation (1/2/3/4): ")

if user_input in calculator:
    print(f"You selected: {calculator[user_input]}")
else:
    print("Invalid input. Please select a valid operation.")

if user_input in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if user_input == '1':
        print(f"Result: {addition(num1, num2)}")
    elif user_input == '2':
        print(f"Result: {subtraction(num1, num2)}")
    elif user_input == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif user_input == '4':
        print(f"Result: {division(num1, num2)}")


