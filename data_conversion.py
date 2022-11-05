import csv
import sqlite3
from queries.sql_creation import inserts, creations, inDB


conn = sqlite3.connect("db/CSMatchData.db")
cursor = conn.cursor()

# Contains filepaths and databases named after them
filepaths = [("data/economy.csv", "Economies"),
             ("data/picks.csv", "Picks"),
             ("data/players.csv", "Players"),
             ("data/results.csv", "Results")]


def createTable(tableName: str):
    query = creations[tableName]
    cursor.execute(query)
    conn.commit()


def tableExists(tableName: str):
    res = cursor.execute(inDB, [tableName])
    if (len(res.fetchall())) == 0:
        return False
    else:
        return True


def insert(tableName: str, data: list[str]):
    query = inserts[tableName]
    cursor.execute(query, data)


for file in filepaths:
    print(f"Reading ${file[0]}")

    with open(file[0]) as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_headings = next(csv_reader)
        if not tableExists(file[1]):
            createTable(file[1])
        index = 0
        for line in csv_reader:
            try:
                insert(file[1], line)
            except Exception as e:
                print(f"Error index: {index}")
                print(f"Error line data: {line}")
                print(f"Error: {e}")
                print("Quitting Program")
                quit()
            index += 1
            if index % 10000 == 0:
                print(" lines traversed")
                conn.commit()
        conn.commit()

conn.close()
