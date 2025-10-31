tasks = dict()
stats = dict()

def create_task(description):
    if not tasks:
        new_id = 1
    else:
        new_id = max(tasks.keys()) + 1
    tasks[new_id] = description
    stats[new_id] = False
    return new_id

def show_tasks():
    print("\n=== Your Todo List ===")
    if not tasks:
        print("No tasks yet!")
        return
    for tid in tasks:
        if not stats[tid]:
            print(f"{tid}: {tasks[tid]} - Not Completed")

def complete_task(tid):
    if tid in stats:
        stats[tid] = True
        return True
    return False

def delete_task(tid):
    if tid in tasks and tid in stats:
        del tasks[tid]
        del stats[tid]
        return True
    return False

def main():
    while True:
        print("\n=== Todo Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            name = input("Enter task description: ")
            task_id = create_task(name)
            print(f"Added task #{task_id}: {name}")
        elif choice == "3":
            try:
                tid = int(input("Enter task ID to complete: "))
                success = complete_task(tid)
                if success:
                    print(f"Task #{tid} marked as completed!")
                else:
                    print("Invalid task ID.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                tid = int(input("Enter task ID to delete: "))
                success = delete_task(tid)
                if success:
                    print(f"Task #{tid} deleted.")
                else:
                    print("Invalid task ID.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
