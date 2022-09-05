# for the terminal output
# we need the console and the table
from turtle import pos
from rich.console import Console
from rich.table import Table

# for creating the command line interface
import typer

# for creating the database so that we can store the tasks and the other info
import sqlite3

# importing the database definitions we made
from model import TaskTracker

# importing all the database function which were created
from database import insert_task, delete_task, get_all_tasks, update_task, complete_task

# creating a console object
console = Console()

# creating a typer object
app = typer.Typer()

# the app.commands() and the corresponding functions help us deal with the CLI (command line interface) 
# we basically create our command
# with the ability to display the appropriate success and error messages for the commands
# the short_help parameter helps us to add a description for the tasks
# the function name is the command name in the cmd and it has its arguments
# if the appropriate arguments are not passed then an error or helper message is displayed
# if the the approproate arguments are passed then whatever is inside the function will be executed
# in this case inside the function we display an appropriate success message

# function for adding a task
@app.command(short_help='adds a task')
def add(task: str, category: str):
    # prints in the command line
    typer.echo(f"adding the {task} task in the {category} category")
    
    # creating a task tracker object (function from model.py) and 
    # insert the input in the appropriate attributes in the database (function from databse.py)
    todo = TaskTracker(task, category)
    insert_task(todo)
    
    # calls the display function to print the table
    display()
    
# function for deleting a task
@app.command(short_help='deletes a task')
def delete(position: int):
    # prints in the command line
    typer.echo(f"deleting {position}")
    
    # deletes the task at the given position (function from database.py)
    # we do position - 1 instead of position because the indices in the UI start at 1 but in the database we begin at 0
    delete_task(position - 1)
    
    # calls the display function to print the table
    display()
    
# function for updating a task
@app.command(short_help='updates a task')
def update(position: int, task: str=None, category: str=None):
    # prints in the command line
    typer.echo(f"updating {position}")
    
    # updates the task at the given position (function from database.py)
    # we do position - 1 instead of position because the indices in the UI start at 1 but in the database we begin at 0
    update_task(position-1, task, category)
    
    # calls the display function to print the table
    display()
    
# function for completing a task
@app.command(short_help='marks a task as complete')
def complete(position: int):
    # prints in the command line
    typer.echo(f"complete {position}")
    
    # marks the task as complete at the given positon (function from database.py)
    # we do position - 1 instead of position because the indices in the UI start at 1 but in the database we begin at 0
    complete_task(position-1)
    
    # calls the display function to print the table
    display()
    
# function for showing the tasks
@app.command(short_help='displays the tasks')
def display():
    # we get all the tasks from the database (function from database.py)
    # this will contain a list of TaskTracker objects and each object will contain the appropriate attributes from model.py
    tasks = get_all_tasks()
    
    # printing a name for the table with the color magenta and making the text bold
    # an opening and closing tag [] [/] is needed for the fonts etc
    console.print("[bold magenta]TODO LIST[/bold magenta]!", "💻")
    
    # creating a table with appropriate columns
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("TASK", min_width=20)
    table.add_column("CATEGORY",  min_width=12, justify="right")
    table.add_column("STATUS", min_width=12, justify="right")
    
    # looping through the tasks with initial index as 1
    for index, task in enumerate(tasks, start=1):
        # getting the color code of a category 
        c = get_category_color(task.category)
        # checks if the task is done of not and adds the appropriate emoji
        if task.status == 2:
            task_flag = '✔'
        else:
            task_flag = '❌'
        # adding a row to the table
        # the row contains the index, the name of the task,
        # the category of the task with the appropriate color coding for the category and the emoji dependent on whether a task is completed or not
        table.add_row(str(index), task.task, f'[{c}]{task.category}[/{c}]', task_flag)
        
    # for printing the table
    console.print(table)


def get_category_color(category):
    """
        Function to find the apprpriate color for a category
        Returns a color based on its presence in the dictionary
        
        Args:
            category (str): _a category for the taks

        Returns:
            str: a color for the category
    """
    COLORS = {"COLLEGE": "red", "OUTSIDE COLLEGE": "blue", "TIMEPASS":"green", "HOME":"cyan"}
    if category in COLORS:
        return COLORS[category]
    return 'white'


if __name__=="__main__":
    app()