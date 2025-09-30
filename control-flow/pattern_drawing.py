# pattern_drawing.py
# Draw a square pattern of asterisks using nested loops

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for each row
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    # Increment the row counter
    row += 1
