#!/usr/bin/env python

"""
Titanic Queries with PostgreSQL
"""

"""
Practice! Go back to both your deployed PostgreSQL 
(Titanic data) and MongoDB (RPG data) instances - use 
MongoDB queries to answer the same questions as you did 
from the first module (when the RPG data was in SQLite). 
With PostgreSQL, answer the following:
"""

import pandas as pd
import psycopg2
import sqlite3

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()
df.to_sql('titanic', conn)


# How many passengers survived, and how many died?

# Survived
query = curs.execute("""
SELECT COUNT (*) 
FROM titanic 
WHERE survived = 1;"""
)
lived = curs.fetchall()[0][0]
print(lived, 'passangers survived')

# Died
query = curs.execute("""
SELECT COUNT (*) 
FROM titanic 
WHERE survived = 0;"""
)
died = curs.fetchall()[0][0]
print(died, 'passangers died')



# How many passengers were in each class?

# Class 1
query = curs.execute("""
SELECT COUNT (*) 
FROM titanic 
WHERE pclass = 1;"""
)
class1 = curs.fetchall()[0][0]

# Class 2
query = curs.execute("""
SELECT COUNT (*) 
FROM titanic 
WHERE pclass = 2;"""
)
class2 = curs.fetchall()[0][0]

# Class 3
query = curs.execute("""
SELECT COUNT (*) 
FROM titanic 
WHERE pclass = 3;"""
)
class3 = curs.fetchall()[0][0]

print('There were', class1, 'class 1 passengers,', class2,
      'class 2 passengers and,', class3, " class 3 passengers.")



# How many passengers survived/died within each class?

for _ in range(1, 4):
  # Survived by class
  query = """
  SELECT COUNT (*) 
  FROM titanic 
  WHERE pclass = """ + str(_) + """ 
  AND survived = 1;"""
  curs.execute(query)
  pclass_lived = curs.fetchall()[0][0]
  print(pclass_lived, 'passengers survived from class', _)

  # Died by class
  query = """
  SELECT COUNT (*) 
  FROM titanic 
  WHERE pclass = """ + str(_) + """ 
  AND survived = 0;"""
  curs.execute(query)
  pclass_died = curs.fetchall()[0][0]
  print(pclass_died, 'passengers died from class', _)
  


# What was the average age of survivors vs nonsurvivors?

# Average age of survivor
query = curs.execute("""
SELECT AVG(age) 
FROM titanic 
WHERE survived=1;"""
)
age_lived = curs.fetchall()[0][0]
print('The average age of survivor is:', age_lived)

# Average age of non-survivor
query = curs.execute("""
SELECT AVG(age) 
FROM titanic 
WHERE survived=0;"""
)
age_died = curs.fetchall()[0][0]
print('The average age of non-survivor is:', age_died)



# What was the average age of each passenger class?
for _ in range(1,4):
  query = """
  SELECT AVG(age) 
  FROM titanic 
  WHERE pclass= """ + str(_) + """;
  """
  curs.execute(query)
  pclass_age = curs.fetchall()[0][0]
  print('The average age of class ', _, 'is', pclass_age)



# What was the average fare by passenger class? 
for _ in range(1,4):
  query = """
  SELECT AVG(fare) 
  FROM titanic 
  WHERE pclass= """ + str(_) + """;
  """
  curs.execute(query)
  pclass_fare = curs.fetchall()[0][0]
  print('The average fare for class', _, 'is', pclass_fare)


# What was the average fare by survival?
query = curs.execute("""
SELECT AVG(fare) 
FROM titanic 
WHERE survived=1;"""
)
fare_lived = curs.fetchall()[0][0]
print('The average fare by survival is', fare_lived)


# How many siblings/spouses aboard on average, by passenger class? 
for _ in range(1,4):
  query = """
  SELECT AVG(sibling_spousesaboard) 
  FROM titanic 
  WHERE pclass= """ + str(_) + """;
  """
  curs.execute(query)
  sib_class = curs.fetchall()[0][0]
  print('The average number of siblings aboard for class', _, 'is', sib_class)


# How many siblings/spouses aboard on average, by survival?
query = curs.execute("""
SELECT AVG(sibling_spousesaboard) 
FROM titanic 
WHERE survived=1;"""
)
ss_lived = curs.fetchall()[0][0]
print('The average number of siblings/spouses aboard by survival', ss_lived)


# How many parents/children aboard on average, by passenger class? 
for _ in range(1,4):
  query = """
  SELECT AVG(parents_childrenaboard) 
  FROM titanic 
  WHERE pclass= """ + str(_) + """;
  """
  curs.execute(query)
  pc_avg = curs.fetchall()[0][0]
  print('The average number of parents/children aboard for class', _, 'is', pc_avg)


# How many parents/children aboard on average, by survival?
query = curs.execute("""
SELECT AVG(parents_childrenaboard) 
FROM titanic
WHERE survived=1;"""
)
pc_lived = curs.fetchall()[0][0]
print('The average number of parents/children aboard by survival is', pc_lived)


# Do any passengers have the same name?
query = curs.execute("""
SELECT COUNT(name) 
FROM titanic
GROUP BY name 
HAVING ( COUNT(name) > 1 );"""
)
names = curs.fetchall()
print('There were', names, 'passengers with the same name')