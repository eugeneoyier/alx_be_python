# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1
