inventory = {}

def add_item():
  user_add = input("Item name: ")
  item_addquantity = int(input("item quantity: "))
  try:
    inventory.update({user_add: item_addquantity})
  except ValueError:
    print("Plaese enter only number")
  print(f"You've added {item_addquantity} of {user_add} to your inventory manager list")
  
def remove_item():
  user_remove = input("Item name: ")
  if user_remove not in inventory:
    print("Item not found")
    return
  remove_quanity = int(input("remove quanity: "))
  if remove_quanity == inventory[user_remove]:
    inventory.pop({user_remove})
    print(f"You've completely remove {user_remove} from your inventory manager list")
  else:
    inventory[user_remove] -= remove_quanity
    print(f"You've remove {remove_quanity} of {user_remove} from you manager list, remaining {inventory[user_remove]} left")
  
def view_item():
  if not inventory:
      print("Nothing in inventory")
  else:
      print("Inventory:")
      for item, qty in inventory.items():
          print(f"{item}: {qty}")
      print()

print("Welcome to the inventory tracker")
while True:
  print("="*50)
  user_choice = int(input("| 1. ADD ITEM | 2. VIEW ITEM | 3. REMOVE | 4. EXIT | (1|2|3|4): "))
  print("="*50)

  if user_choice == 1:
    add_item()
  elif user_choice == 2:
    view_item()
  elif user_choice == 3:
    remove_item()
  elif user_choice == 4:
    print("Have a nice day")
    break
  else:
    print("1-4")
  