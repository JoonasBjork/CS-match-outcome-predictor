import sqlite3
from queries.sql_creation import drop_table
from utils.error_handlers import operational_error_print
from utils.lists import drop_table_list

from utils.path import get_project_root
# Script to delete all db tables
# In case that data is partly converted and the program crashed


def main():

    with sqlite3.connect(f"{get_project_root()}/db/CSMatchData.db") as conn:
        cur = conn.cursor()

        for table_name in drop_table_list:
            print(f"Removing table \"{table_name}\"")
            try:
                cur.execute(drop_table.replace("?", table_name))
                conn.commit()
                print(f"Successful")
            except sqlite3.OperationalError as e:
                operational_error_print(table_name, e)


if __name__ == "__main__":
    main()
