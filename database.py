# sqlite3 pachage for the database
import sqlite3

from typing import List

# importing our model class
from model import task_tracker

import datetime

# creating a connection and definining a name for the database
connection = sqlite3.connect('task_tracker.db')

# creating a cursor
cursor = connection.cursor()

# defining the table and the same attributes as the ones in model.py
# we also define the datatypes of the attributes related to sqlite like string datatype is text here
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_tracker ()
        task text,
        category text.
        data_added text
        status integer
        position integer
        )
        """)

# for insterting tasks
def insert_task(task: task_tracker):
    cursor.execute('select count(*) FROM todos')
    count = cursor.fetchone()[0]
    task.position = count if count else 0
    with connection:
        cursor.execute('INSERT INTO task_tracker VALUES (:task, :category, :data_added, :data_completed, :status, :position)',
                       {'task':task.task, 'category':task.category, 
                        'data_added':task.date_added, 'date_ccompleted':task.date_completed,
                        'status':task.status, 'position':task.position})
    

# calling the create table function
create_table()
