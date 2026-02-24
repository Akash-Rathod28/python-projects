todo = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo.append(task)
        print("Task added successfully")

    elif choice == '2':
        print("Your Tasks:")
        for i in range(len(todo)):
            print(i+1, ".", todo[i])

    elif choice == '3':
        print("Thank you for using To-Do List")
        break

    else:
        print("Invalid choice")
