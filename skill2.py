tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task: ")
        pr = input("Enter your priority (High/Medium/Low): ").capitalize()
        t = {"task": task, "priority": pr}
        tasks.append(t)
        print("Task added!")

    elif choice == 2:
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for task in tasks:
                print(f"Task: {task['task']}  | Priority: {task['priority']}")

    elif choice == 3:
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please try again.")
