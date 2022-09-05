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
    # defining the parameter from befor can prevent SQL Injection attacks
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
    
# calling the create table function
create_table()
