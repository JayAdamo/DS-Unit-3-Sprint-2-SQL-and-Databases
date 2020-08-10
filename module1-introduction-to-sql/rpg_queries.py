#!/usr/bin/env python

import sqlite3

"""
QUERIES FOR THE RPG DATABASE
"""
# Connecting and importing the database
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

"""
QUERIES
"""

# How many total Characters are there?
chars = curs.execute("""
SELECT COUNT(*) FROM charactercreator_character;"""
).fetchall()[0][0]
print('Total number of characters:', chars)

# How many of each specific subclass?
clerics = curs.execute("""
SELECT COUNT(*) FROM charactercreator_cleric;"""
).fetchall()[0][0]
print('Total number of clerics:', clerics)

fighters = curs.execute("""
SELECT COUNT(*) FROM charactercreator_fighter;"""
).fetchall()[0][0]
print('Total number of fighters:', fighters)

mages = curs.execute("""
SELECT COUNT(*) FROM charactercreator_mage;"""
).fetchall()[0][0]
print('Total number of mages:', mages)

necros = curs.execute("""
SELECT COUNT(*) FROM charactercreator_necromancer;"""
).fetchall()[0][0]
print('Total number of necromancers:', necros)

thieves = curs.execute("""
SELECT COUNT(*) FROM charactercreator_thief;"""
).fetchall()[0][0]
print('Total number of thieves:', thieves)

# How many total Items?
items = curs.execute("""
SELECT COUNT(*) FROM armory_item;"""
).fetchall()[0][0]
print('Total number of items:', items)

# How many of the Items are weapons? How many are not?
weapons = curs.execute("""
SELECT COUNT(*) FROM armory_weapon;"""
).fetchall()[0][0]
print('Total number of weapons:', weapons)
print('Total number of non-weapons:', (items - weapons))

# How many Items and weapons does each character have? (Return first 20 rows)
char_items = ("""
SELECT COUNT (*) 
FROM charactercreator_character 
JOIN charactercreator_character_inventory 
ON charactercreator_character.character_id = charactercreator_character_inventory.character_id 
GROUP BY charactercreator_character_inventory.character_id;"""
)

char_weapons = ("""
SELECT COUNT (*) 
FROM charactercreator_character 
JOIN charactercreator_character_inventory 
ON charactercreator_character.character_id = charactercreator_character_inventory.character_id 
JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id 
GROUP BY charactercreator_character_inventory.character_id;"""
)
x = range(0, 20)
for _ in x:
    print('Character', _ + 1, 'has', curs.execute(char_items).fetchall()[_][0], 
    'items and', curs.execute(char_weapons).fetchall()[_][0], 'weapons')


# On average, how many Items and weapons does each Character have?"""
"""
SELECT AVG(num_items) FROM
(SELECT cc.character_id, COUNT(DISTINCT ai.item_id) AS num_items
FROM charactercreator_character AS cc,
charactercreator_character_inventory AS cci,
armory_item AS ai
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY 1);
"""

y = range(0,302)
test = range(0,155)
item_count = 0
weapon_count = 0
for _ in y:
    item_count = item_count + curs.execute(char_items).fetchall()[_][0]

print("The average items per character is: ", item_count / 302)

for _ in test:
    weapon_count = weapon_count + curs.execute(char_weapons).fetchall()[_][0]

print("The average weapons per character is: ", weapon_count / 155)

