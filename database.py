# sqlite3 pachage for the database
import sqlite3

from typing import List

# importing our model class
from model import TODO 

import datetime

# creating a connection and definining a name for the database
connection = sqlite3.connect('task_tracker.db')

# creating a cursor
cursor = connection.cursor()

# defining the table and the same attributes as the ones in model.py
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_tracker ()
        task text,
        category text.
        data_added text
        status integer
        position integer
        )
        """)

# calling the create table function
create_table()