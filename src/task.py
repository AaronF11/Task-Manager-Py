class Task:
    def __init__(self, title, description, due_date, completed):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        """
        Mark task as completed.
        """
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {status}"
