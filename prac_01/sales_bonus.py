# Question 1: Sales Bonus

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
THRESHOLD = 1000
LOWER_BONUS = 0.1
UPPER_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < THRESHOLD:
        bonus = sales * LOWER_BONUS
    else:
        bonus = sales * UPPER_BONUS
    print(f"User's bonus based on sales is ${bonus:.2f} ")
    sales = float(input("Enter sales: $"))
