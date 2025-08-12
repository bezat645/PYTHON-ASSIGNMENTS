num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
op = input("Enter an operation (+, -, *, /): ")  

def calculate(num1, num2, op):
    while True:
        if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
            break
        else:
            print("Invalid input for the  number. Please enter a valid number.")
            num1 = input("Enter a number: ")
            num2 = input("Enter another number: ")  
    while True:
        if op in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            op = input("Enter an operation (+, -, *, /): ")
    
    num1 = float(num1)
    num2 = float(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
      

result = calculate(num1, num2, op)
print(result)




