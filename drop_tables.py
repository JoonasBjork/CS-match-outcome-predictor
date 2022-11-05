import sqlite3
from queries.sql_creation import drop_table
from error_handlers import operationalErrorPrint

# Script to delete all db tables
# In case that data is partly converted and the program crashed
tableNames = ["Economies",
              "Picks",
              "Players",
              "Results"]

conn = sqlite3.connect("db/CSMatchData.db")
cur = conn.cursor()


for tableName in tableNames:
    print(f"Removing table \"{tableName}\"")
    try:
        cur.execute(drop_table.replace("?", tableName))
        conn.commit()
    except sqlite3.OperationalError as e:
        operationalErrorPrint(tableName, e)

conn.close()
