# Prompt user for input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume 5% annual interest rate and calculate projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year including interest: {projected_savings}")
