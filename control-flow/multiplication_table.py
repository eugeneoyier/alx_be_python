# multiplication_table.py
# Generate multiplication table using a for loop

# Prompt the user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
