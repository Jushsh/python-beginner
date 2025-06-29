tasks = []
print("Let's start your day")

while True:
  choice = input("Choose an action: add task, view tasks, remove task, or quit: ")
  if choice == "add task":
    task = input("Enter your task for today: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
  elif choice == "view tasks":
    if not tasks:
      print("No tasks yet.")
    else:
      print("Tasks:")
      for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
  elif choice == "remove task":
    if not tasks:
      print("No tasks to remove.")
    else:
      try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
          removed_task = tasks.pop(index)
          print(f"Task '{removed_task}' removed.")
        else:
          print("Invalid task number.")
      except ValueError:
        print("Invalid input. Please enter a number.")
  elif choice == "quit":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please choose 'add task', 'view tasks', 'remove task', or 'quit'.")