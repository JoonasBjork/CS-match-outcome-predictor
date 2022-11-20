import sqlite3
from queries.sql_creation import sql_get_raw_round_economies, creations, inserts
from utils.path import get_project_root
from utils.error_handlers import integrity_error_print
from utils.lists import map_encodings
from db_operations import insert_into_table, table_exists, create_table

# Convert the data into form
# match_id, round_num, t1_score, t2_score, t1_side, t2_side, t1_equip_value, t2_equip_value, equip_value_difference, map, round_winner, game_winner

project_root = get_project_root()

# Name of the created table that contains the finalized data
_TABLE_NAME = "Rounds"


def main():
    try:
        conn = sqlite3.connect(f"{project_root}/db/CSMatchData.db")
        cursor = conn.cursor()

        if not table_exists(cursor, _TABLE_NAME):
            create_table(conn, creations[_TABLE_NAME])

        # Get raw table data from combined tables
        cursor.execute(sql_get_raw_round_economies)

        names = [description[0] for description in cursor.description]

        # All indices in the raw data that are filtered into processed data
        match_id_index = names.index('match_id')
        round_winner_index = names.index('round_1_winner')
        t1_start_index = names.index('t1_start')
        map_index = names.index('_map')
        t1_economies_index = names.index('round_1_t1')
        t2_economies_index = names.index('round_1_t2')
        game_winner_index = names.index('match_winner')

        index = 1

        for row in cursor.fetchall():
            round_count = 30 - \
                (row[round_winner_index:round_winner_index + 30]).count('')
            current_t1_wins = 0
            current_t2_wins = 0
            for round_num in range(0, round_count):

                # 0: t-side, 1: ct-side
                t1_side = 0
                t2_side = 1

                if ((row[t1_start_index] == 't') != (round_num < 15)):
                    t1_side = 1
                    t2_side = 0

                data = [row[match_id_index],
                        round_num,
                        current_t1_wins,
                        current_t2_wins,
                        t1_side,
                        t2_side,
                        row[t1_economies_index + round_num],
                        row[t2_economies_index + round_num],
                        row[t1_economies_index + round_num] -
                        row[t2_economies_index + round_num],
                        map_encodings[row[map_index]],
                        row[round_winner_index + round_num],
                        row[game_winner_index]
                        ]

                insert_into_table(
                    cursor, inserts[_TABLE_NAME], data)
                if (index % 10000 == 0):
                    print(f"{index} lines added")
                index += 1

                if (row[round_winner_index + round_num] == 1):
                    current_t1_wins += 1
                else:
                    current_t2_wins += 1
    except sqlite3.IntegrityError as e:
        integrity_error_print(index, e)
    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
