from src.task import Task
from src.task_manager import TaskManager


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date, False)  # False: Task is initially not completed
            task_manager.add_task(task)
            print("Task added successfully!")
        elif choice == "2":
            print("\nAll Tasks:")
            task_manager.display_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_as_completed(index)
        elif choice == "4":
            index = int(input("Enter task number to remove: "))
            task_manager.remove_task(index)
            print("Task removed successfully!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
