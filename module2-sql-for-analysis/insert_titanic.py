#!/usr/bin/env python

"""
Create table for titanic.csv
"""

import pandas as pd
import psycopg2
import sqlite3

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")
#print(df.shape)

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()
df.to_sql('titanic', conn)

titanic_data = 'SELECT * FROM titanic;'
passengers = curs.execute(titanic_data).fetchall()

dbname = 'wjrrzomz'
user = 'wjrrzomz'
password = '1sPo0pGh_oWREF3Q-A7Y1tjSchjSVIeA'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

create_table_statement = """
CREATE TABLE titanic_new (
    id SERIAL PRIMARY KEY,
    survived INTEGER,
    pclass INTEGER,
    name VARCHAR(120),
    sex VARCHAR(10),
    age FLOAT(1),
    sibling_spouse_aboard INTEGER,
    parents_children_aboard INTEGER,
    fare FLOAT(4)
);
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(create_table_statement)


for passenger in passengers:
    insert_passenger = """
    INSERT INTO titanic_new
    (survived, pclass, name, sex, age, 
    sibling_spouse_aboard, parents_children_aboard, fare)
    VALUES""" + str(passenger[1:]) + ";"
    pg_curs.execute(insert_passenger)

pg_conn.commit()