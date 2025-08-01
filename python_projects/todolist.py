# todolist.py

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("🟡 No tasks yet.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    print("=== Welcome to Sanjay's To-Do List App ===")

    while True:
        print("\nChoose an option:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Exit")

        choice = input("Enter 1, 2 or 3: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter your new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added!")
        elif choice == "3":
            print("👋 Goodbye! Tasks saved.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()