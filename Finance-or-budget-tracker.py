
print("Welcome to my budget tracker")
transactions = []
balance = 0.00

while True:
    print("\n" + "="*50)
    print("OPTIONS: Add income | Add expense | Show balance | View all transactions | Exit")
    print("="*50)
    user_choice = input("Enter your choice: ").lower().strip()
    
    if user_choice == "add income":
        try:
            user_income = float(input("Enter your income: $"))
            balance += user_income
            transactions.append(("Income", user_income))
            print(f"Income of ${user_income:.2f} added. Your balance is now ${balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif user_choice == "add expense":
        try:
            user_expense = float(input("Enter your expense: $"))
            balance -= user_expense
            transactions.append(("Expense", user_expense))
            print(f"Expense of ${user_expense:.2f} recorded. Your balance is now ${balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == "show balance":
        print(f"Your current balance is: ${balance:.2f}")

    elif user_choice == "view all transactions":
        if not transactions:
            print("No transactions recorded yet.")
        else:
            print("\n--- Transaction History ---")
            for i, (transaction_type, amount) in enumerate(transactions, 1):
                print(f"{i}. {transaction_type}: ${amount:.2f}")
            print(f"\nTotal transactions: {len(transactions)}")
            
    elif user_choice == "exit":
        print("Thank you for using the budget tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
