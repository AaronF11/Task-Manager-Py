class Task:

    def __init__(self, title, description, due_date, completed):
        """
        Initialize the Task object with title, description, due date, and completion status.

        Parameters:
        - title (str): The title of the task.
        - description (str): The description of the task.
        - due_date (str): The due date of the task.
        - completed (bool): The completion status of the task.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def completed(self):
        """
        Mark task as completed.
        """
        self.completed = True

    def __str__(self):
        """
        Return a string representation of the task.

        Returns:
        - str: A formatted string containing the title, description, due date, and status of the task.
        """
        status = "Done" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {status}"
