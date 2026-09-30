# Riley Kotter
# IS 303 - Level 4 Assignment
# This program analyzes a list of personal expenses.

expenses = []

# Ask for the first expense
expense = float(input("Enter an expense or 0 to finish: "))

# Keep asking until the user enters 0
while expense != 0:
    if expense < 0:
        print("Expenses cannot be negative. Please try again.")
    else:
        expenses.append(expense)
    expense = float(input("Enter an expense or 0 to finish: "))

# Only show a summary if at least one expense was entered
if len(expenses) == 0:
    print("No expenses were entered.")
else:
    # Set up the variables for the summary
    total = 0
    small = 0
    moderate = 0
    large = 0
    smallest = expenses[0]
    largest = expenses[0]

    # Go through each expense
    for amount in expenses:
        total = total + amount

        # Classify the expense
        if amount < 25:
            small = small + 1
        elif amount <= 100:
            moderate = moderate + 1
        else:
            large = large + 1

        # Check for smallest and largest
        if amount < smallest:
            smallest = amount
        if amount > largest:
            largest = amount

    count = len(expenses)
    average = total / count

    # Print the results
    print()
    print("Expense Summary")
    print("---------------")
    print(f"Number of expenses: {count}")
    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Smallest expense: ${smallest:,.2f}")
    print(f"Largest expense: ${largest:,.2f}")
    print(f"Small expenses: {small}")
    print(f"Moderate expenses: {moderate}")
    print(f"Large expenses: {large}")
