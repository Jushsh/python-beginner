Balance = 0.00
transaction = []

def deposit():
  global Balance
  dep_amount = float(input("Enter your amount: $"))
  Balance += dep_amount
  transaction.append(("Fund In", dep_amount))
  print(f"You have deposit ${dep_amount:.2f} to your balance")

def withdraw():
  global Balance
  wi_amount = float(input("withdrawal amount: $"))
  if wi_amount > Balance:
    print("inssuficient amount/Not enough Money to be deposited")
  else:
    Balance -= wi_amount
    transaction.append(("Withdrawed", wi_amount))
    print(f"You have withdrawed ${wi_amount:.2f} to your balance")
    
def view_balance():
  print(f"Current balance ${Balance:.2f}")

def view_transaction():
  if not transaction:
    print("No transaction currently")
  else:
    for t_type, amount in transaction:
      print(f"{t_type}: {amount}")

Active = True

print("Welcome back")
while Active == True:
  try:
    print("="*50)
    user_choice = int(input("1. DEPOSIT | 2. WITHDRAW | 3. VIEW BALANCE | 4. VIEW TRANSACTION | 5. EXIT | (1-4): "))
    print("="*50)
  except Exception:
    print("only 1 - 4")

  if user_choice == 1:
    deposit()
  elif user_choice == 2:
    withdraw()
  elif user_choice == 3:
    view_balance()
  elif user_choice == 4:
    view_transaction()
  elif user_choice == 5:
    print("have a nice day")
    break