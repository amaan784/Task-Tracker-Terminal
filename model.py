# the purpose of this file is to define our database, define tables, fields

# datetime module 
import datetime

class TaskTracker:
    def __init__(self, task, category, date_added=None, date_completed=None, status=None, position=None):
        """
        Constructor for the todo / task tracker app / table

        Args:
            task (str): name of the task
            category (str): category of the task
            date_added (str, optional): the date the task was added to the table. Defaults to None.
            date_completed (str, optional): the date that task was completed. Defaults to None.
            status (int, optional): flag for checking whether a task was completed . Defaults to None.
            position (int, optional): the position / index at which the task will be stored. Defaults to None.
        """
        self.task = task
        self.category = category
        self.status = status if status is not None else 1 # 1 = not completed, 2 = completed
        self.position = position if position is not None else None
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat() # isoformat changes the datatype to str from datetime.datetime
        self.date_completed = date_completed if date_completed is not None else None
        
    def __repr__(self) -> str:
        """
        For printing the object

        Returns:
            str: returns the contents of the object
        """
        return f"({self.task}, {self.category}, {self.status}, {self.position}, {self.date_added}, {self.date_completed})"