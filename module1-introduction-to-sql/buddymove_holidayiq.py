#!/usr/bin/env python

"""
Buddy csv
"""

import pandas as pd
import sqlite3

# Count how many rows you have (should be 249)
df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
df.to_sql('review', conn)

counts = """SELECT COUNT (*) FROM review;"""

# How many users who reviewed at least 100 'Nature' also reviewed 
# at least '100' in Shopping.
print("Total number of users:", curs.execute(counts).fetchall()[0][0])

assign2 = """SELECT COUNT (*) FROM review WHERE Nature >= 100 AND Shopping >= 100"""

print("Users who had at least 100 in both nature and shopping", curs.execute(assign2).fetchall()[0][0])
