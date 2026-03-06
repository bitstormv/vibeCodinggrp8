# Monthly Budget Tracker

while True:
    # Ask the user to input their total monthly budget
    budget_input = input("Enter your total monthly budget (or press Enter to exit): ")
    if budget_input == "":
        print("Exiting program.")
        exit()
    budget = float(budget_input)

    # Initialize total expenses
    total_expenses = 0
    expense_count = 0

    # Loop to allow multiple expense entries
    print("\nEnter your expenses (type 'done' when finished):\n")
    while True:
        expense_input = input(f"Enter expense #{expense_count + 1} amount (or 'done' to finish): ")
        
        # Check if user wants to exit the expense loop
        if expense_input.lower() == 'done':
            break
        
        # Check if user pressed Enter to exit entire program
        if expense_input == "":
            print("Exiting program.")
            exit()
        
        try:
            expense = float(expense_input)
            if expense < 0:
                print("Warning: Expense is an invalid number. Please enter a valid positive amount.")
                continue
            total_expenses += expense
            expense_count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
            continue

    # Calculate remaining balance
    remaining_balance = budget - total_expenses

    # Display summary
    print("\n----- Monthly Budget Summary -----")
    print(f"Total Budget: Rs.{budget:.2f}")
    print(f"Total Expenses: Rs.{total_expenses:.2f}")
    print(f"Remaining Balance: Rs.{remaining_balance:.2f}")

    # Conditional check for low funds
    if remaining_balance < 500:
        print("\nWarning: Low Funds")

    # Ask whether to exit or restart
    again = input("\nWould you like to exit the program? (y/n): ")
    if again.lower() == 'y':
        print("Exiting program.")
        break
    print("\nRestarting...\n")
