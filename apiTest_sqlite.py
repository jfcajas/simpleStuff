import requests
import sqlite3
from pprint import pprint

response = requests.get('https://api.publicapis.org/entries')

obj = response.json()

api_objs = [x['API'] for x in obj['entries'] if x['API'] != 'null'] # list comprehension

api_names = [x for x in api_objs if x[0] == 'S'] # selecting just those that begin with S

api_ids = []
for i in range(len(api_names)):
    api_ids.append(i+1)

apiLen = len(api_ids)
pprint(apiLen)
pprint(api_names) 

# define connection and connect to sqlite database

conn = sqlite3.connect('../pythonProject2/storage.db') # need to redefine this

cursor = conn.cursor()
# drop the table to create new one
dropTables = """DROP TABLE IF EXISTS apis_table"""
cursor.execute(dropTables)
command1 = """CREATE TABLE apis_table (api_ids text primary key, api_names text)"""
cursor.execute(command1)


# add in values
for x in range(0, apiLen):
    cursor.execute("""INSERT INTO apis_table (api_ids, api_names) VALUES (?, ?)""",
                   (str(api_ids[x]), str(api_names[x])))
    conn.commit()

# get data

for row in cursor.execute('SELECT * FROM apis_table ORDER BY api_ids'):
    pprint(row)

conn.close()
