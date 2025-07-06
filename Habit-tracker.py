habits = []
print("Welcome to THE HABIT TRACKER 2.0")

while True:
    choice = input("Choose: add habit, mark as done, view habits, or quit: ").lower()

    if choice == "add habit":
        habit_name = input("Enter the habit you want to track: ")
        habits.append({"name": habit_name, "done": False})
        print(f"You've added '{habit_name}' to your habit list.")

    elif choice == "view habits":
        if not habits:
            print("No habits yet.")
        else:
            for i, habit in enumerate(habits, start=1):
                status = "Done ✅" if habit["done"] else "Not done ❌"
                print(f"{i}. {habit['name']} - {status}")

    elif choice == "mark as done":
        if not habits:
            print("No habits to mark as done.")
        else:
            for i, habit in enumerate(habits, start=1):
                status = "Done ✅" if habit["done"] else "Not done ❌"
                print(f"{i}. {habit['name']} - {status}")
            try:
                task_number = int(input("Enter the number of the habit to mark as done: "))
                if 1 <= task_number <= len(habits):
                    habits[task_number - 1]['done'] = True
                    print(f"'{habits[task_number - 1]['name']}' marked as done.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")