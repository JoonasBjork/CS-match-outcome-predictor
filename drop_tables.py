import sqlite3
from queries.sql_creation import drop_tables

# Script to delete all db tables
# In case that data is partly converted and the program crashed

conn = sqlite3.connect("db/CSMatchData.db")
cur = conn.cursor()

cur.executescript(drop_tables)
conn.commit()
conn.close()
