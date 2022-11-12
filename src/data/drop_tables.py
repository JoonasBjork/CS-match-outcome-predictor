import sqlite3
from queries.sql_creation import drop_table
from utils.error_handlers import operationalErrorPrint, fileNotFoundErrorPrint

from utils.path import get_project_root
# Script to delete all db tables
# In case that data is partly converted and the program crashed


def main():
    tableNames = ["Economies",
                  "Picks",
                  "Players",
                  "Results"]

    # filename = Path("asd")
    # print(filename)

    try:
        conn = sqlite3.connect(f"{get_project_root()}/db/CSMatchData.db")
        print(conn)
        cur = conn.cursor()

        for tableName in tableNames:
            print(f"Removing table \"{tableName}\"")
            try:
                cur.execute(drop_table.replace("?", tableName))
                conn.commit()
                print(f"Successfull")
            except sqlite3.OperationalError as e:
                operationalErrorPrint(tableName, e)
    except FileNotFoundError as e:
        fileNotFoundErrorPrint(tableName, e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
