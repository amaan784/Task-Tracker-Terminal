# Task Tracker Terminal
 A task tracker app / table made for the terminal using Python
 
# Files purpose-
 > 1) main.py = main program (contains cmd arguments handling, output etc)
 > 2) model.py = class containing the tasks definition
 > 3) database.py = contains all database functions

# Libraries used-
sqlite3 
typer
rich
datetime

# Instructions-

`git clone https://github.com/amaan784/Task-Tracker-Terminal.git`

`cd task_tracker`

The table will get displayed after each command 

### Displaying the table-
`python main.py display`
 
### Adding a task-
`python main.py add "task" "category"`

### Marking a task as complete-
`python .\main.py complete <position>`

### Deleting a task-
`python .\main.py delete <position>`

### Updating a task name-
`python .\main.py update <position> --task "task"`

### Updating a task category-
`python .\main.py update <position> --category "category"`

### Updating both task name and category-
`python .\main.py update <position> --task "task" --category "category"`


## TODO (how ironic)-
- implement "indepth display" function which will display the the date_added and date_completed attributes
- implement "mark as not complete" function
- implement "delete database" function
- implement "notes" attribute for every task
- implement edge cases like "user giving index which does not exist"
- create a virtual environmet or environment where there wont be the need to write "python .\main.py" again and again

## Sources-

- https://www.youtube.com/watch?v=ynd67UwG_cI
- https://rich.readthedocs.io/en/stable/appendix/colors.html
- https://typer.tiangolo.com/
- https://docs.python.org/3/library/sqlite3.html
