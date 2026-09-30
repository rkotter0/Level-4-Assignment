# Riley Kotter
# IS 303 - Personal Expense Analyzer
# Collects expenses from the user, classifies them, and prints a summary.

expenses = []

# Keep asking for expenses until the user enters 0
while True:
    entry = input("Enter an expense or 0 to finish: ")

    # Make sure the input is a number
    try:
        amount = float(entry)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if amount == 0:
        break
    elif amount < 0:
        print("Expenses cannot be negative. Please try again.")
    else:
        expenses.append(amount)  # add the expense to the list

# Only print a summary if at least one expense was entered
if len(expenses) == 0:
    print("No expenses were entered.")
else:
    # Classify each expense
    small_count = 0
    moderate_count = 0
    large_count = 0

    for expense in expenses:
        if expense < 25:
            small_count += 1
        elif expense <= 100:
            moderate_count += 1
        else:
            large_count += 1

    # Calculate the summary numbers
    num_expenses = len(expenses)
    total = sum(expenses)
    average = total / num_expenses
    smallest = min(expenses)
    largest = max(expenses)

    # Print the results
    print()
    print("Expense Summary")
    print("---------------")
    print(f"Number of expenses: {num_expenses}")
    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Smallest expense: ${smallest:,.2f}")
    print(f"Largest expense: ${largest:,.2f}")
    print(f"Small expenses: {small_count}")
    print(f"Moderate expenses: {moderate_count}")
    print(f"Large expenses: {large_count}")
