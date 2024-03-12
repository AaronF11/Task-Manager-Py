class TaskManager:
    def __init__(self):
        """
        Initialize the TaskManager object with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the task manager.

        Parameters:
        - task (Task): The task to be added to the task manager.
        """
        self.tasks.append(task)

    def display_tasks(self):
        """
        Display all tasks in the task manager.
        """
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_task_as_completed(self, index):
        """
        Mark a task as completed by its index.

        Parameters:
        - index (int): The index of the task to be marked as completed.
        """
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].mark_as_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number. Please try again.")

    def remove_task(self, index):
        """
        Remove a task from the task manager by its index.

        Parameters:
        - index (int): The index of the task to be removed.
        """
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
