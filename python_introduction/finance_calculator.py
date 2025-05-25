# finance_calculator.py

# 1. User Input for Financial Details
# Prompt the user for their monthly income and convert it to a float.
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses and convert it to a float.
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# 2. Calculate Monthly Savings
# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - total_monthly_expenses

# 3. Project Annual Savings
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# Using the simplified formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# 4. Output Results
# Display the user’s monthly savings.
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")