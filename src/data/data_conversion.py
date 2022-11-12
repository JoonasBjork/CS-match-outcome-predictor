import csv
import sqlite3
from queries.sql_creation import inserts, creations, inDB
from utils.path import get_project_root
from utils.error_handlers import integrityErrorPrint, unicodeErrorPrint, fileNotFoundErrorPrint

project_root = get_project_root()


# Contains filepaths and databases named after them
filepaths = [(f"{project_root}/data/raw/economy.csv", "Economies"),
             (f"{project_root}/data/raw/picks.csv", "Picks"),
             (f"{project_root}/data/raw/players.csv", "Players"),
             (f"{project_root}/data/raw/results.csv", "Results")]


def main():
    try:
        conn = sqlite3.connect(f"{project_root}/db/CSMatchData.db")
        cursor = conn.cursor()

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
            print(f"Reading {file[0]}")

            with open(file[0]) as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # skip headings

                if not tableExists(file[1]):
                    createTable(file[1])

                index = 1
                try:
                    for line in csv_reader:
                        try:
                            insert(file[1], line)
                        except sqlite3.IntegrityError as e:
                            integrityErrorPrint(index, line, e)

                        if index % 10000 == 0:
                            conn.commit()
                            print(f"{index} lines added")
                        index += 1

                except UnicodeDecodeError as e:
                    unicodeErrorPrint(index, e)
                conn.commit()
                print(f"END: {index} lines added in total")

    except FileNotFoundError as e:
        fileNotFoundErrorPrint(file[0], e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
