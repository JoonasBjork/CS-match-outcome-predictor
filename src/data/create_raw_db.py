import csv
import sqlite3
from utils.path import get_project_root
from utils.error_handlers import integrityErrorPrint, unicodeErrorPrint
from db_operations import createTable, tableExists, insertIntoTable
from queries.sql_creation import inserts, creations

project_root = get_project_root()


# Contains filepaths and databases named after them
table_paths_and_names = [(f"{project_root}/data/raw/economy.csv", "Economies"),
                         #  (f"{project_root}/data/raw/picks.csv", "Picks"),
                         #  (f"{project_root}/data/raw/players.csv", "Players"),
                         (f"{project_root}/data/raw/results.csv", "Results")]

# Input is a list of tuples
# first value is a filepath, second value is the table name that will be made in the db


def main():
    with sqlite3.connect(f"{project_root}/db/CSMatchData.db") as conn:
        cursor = conn.cursor()

        for file in table_paths_and_names:
            print(f"Reading {file[0]}")

            with open(file[0]) as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # skip headings

                if not tableExists(cursor, file[1]):
                    createTable(conn, creations[file[1]])

                index = 1
                try:
                    for line in csv_reader:
                        try:
                            insertIntoTable(cursor, inserts[file[1]], line)
                        except sqlite3.IntegrityError as e:
                            integrityErrorPrint(index, line, e)

                        if index % 10000 == 0:
                            print(f"{index} lines added")
                        index += 1

                except UnicodeDecodeError as e:
                    unicodeErrorPrint(index, e)
                print(f"END: {index} lines added in total")


if __name__ == '__main__':
    main()
