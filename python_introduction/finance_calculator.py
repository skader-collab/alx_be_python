interest = 0.05  # 5%

# User Input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with Interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest)

# Output Results
print(f"Your monthly savings amount is ${monthly_savings:.2f}")
print(f"After a year with a 5% annual interest rate, your projected annual savings will be ${projected_annual_savings:.2f}")
