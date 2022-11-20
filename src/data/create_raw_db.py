import csv
import sqlite3
from utils.path import get_project_root
from utils.error_handlers import integrity_error_print, unicode_error_print
from db_operations import create_table, table_exists, insert_into_table
from queries.sql_creation import inserts, creations

project_root = get_project_root()


# Contains filepaths and databases named after them
table_paths_and_names = [(f"{project_root}/data/raw/economy.csv", "Economies"),
                         (f"{project_root}/data/raw/picks.csv", "Picks"),
                         (f"{project_root}/data/raw/players.csv", "Players"),
                         (f"{project_root}/data/raw/results.csv", "Results")]


# Input is a list of tuples
# first value is a filepath, second value is the table name that will be made in the db

def main():
    try:
        conn = sqlite3.connect(f"{project_root}/db/CSMatchData.db")
        cursor = conn.cursor()
        index = 1

        for file in table_paths_and_names:
            print(f"Reading {file[0]}")
            index = 1

            with open(file[0]) as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # skip headings

                if not table_exists(cursor, file[1]):
                    create_table(conn, creations[file[1]])

                for line in csv_reader:
                    insert_into_table(cursor, inserts[file[1]], line)

                    if index % 10000 == 0:
                        print(f"{index} lines added")
                    index += 1

                print(f"END: {index} lines added in total")
                index = 1

    except UnicodeDecodeError as e:
        unicode_error_print(index, e)
    except sqlite3.IntegrityError as e:
        integrity_error_print(index, e)
    finally:
        conn.commit()
        conn.close()


if __name__ == '__main__':
    main()
