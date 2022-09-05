# sqlite3 package for the database
import sqlite3

from typing import List

# importing our model class
from model import task_tracker

import datetime

# creating a connection and definining a name for the database
connection = sqlite3.connect('task_tracker.db')

# creating a cursor
cursor = connection.cursor()

# for creating a table
def create_table():
    # defining the table if it does not exist and placing the same attributes as the ones in model.py
    # we also define the datatypes of the attributes related to sqlite like string datatype is text here
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_tracker ()
        task text,
        category text,
        status integer,
        position integer,
        data_added text,
        date_completed text
        )
        """)

# for inserting a task
def insert_task(task: task_tracker):
    # executing sqlite script to count the number of records in the table
    cursor.execute('select count(*) FROM task_tracker')
    # gives the number of items in the table
    count = cursor.fetchone()[0]
    # the position of the task to be inserted is the count of the elements in the table or 0
    task.position = count if count else 0
    # insert the task in the appropriate position
    # defining the parameter from before can prevent SQL Injection attacks
    with connection:
        cursor.execute('INSERT INTO task_tracker VALUES (:task, :category, :status, :position, :data_added, :data_completed)',
                       {'task':task.task, 'category':task.category,
                        'status':task.status, 'position':task.position , 
                        'data_added':task.date_added, 'date_ccompleted':task.date_completed})

# for getting all tasks
def get_all_tasks() -> List[task_tracker]:
    # get all records from the database table
    cursor.execute('select * from task_tracker')
    results = cursor.fetchall()
    tasks = []
    # converting the records one by one to the task_tracker object
    for result in results:
        tasks.append(task_tracker(*result))
    # return the records
    return tasks

# for deleting a task
def delete_task(position):
    # executing sqlite script to count the number of records in the table
    cursor.execute('select count(*) FROM task_tracker')
    # gives the number of items in the table
    count = cursor.fetchone()[0]
    
    with connection:
        # deletes the task which is at the given particular position
        cursor.execute('DELETE from task_tracker WHERE position=:position', {"position:position"})
        # for shifting all the remaining (tasks after the given position) items one position down 
        for pos in range(position + 1, count):
            # calls the function so that the position for every task gets updated
            change_position(pos, pos-1, False)

# for changing the position when deletion of a record happens
def change_position(old_position: int, new_position: int, commit=True):
    # updation of the position happens with the sqlite3 script
    # basicaly replacing the old position with the new position
    cursor.execute('UPDATE task_tracker SET position=:position_new WHERE position=:position_old',
                   {'position_old':old_position}, {'position_new': new_position})
    # this part is like a placeholder since we do not want to commit
    if commit == True:
        connection.commit()
    
# calling the create table function
create_table()
