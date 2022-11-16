import numpy as np
import sqlite3
from queries.sql_creation import sql_get_raw_round_economies, creations, inDB, inserts
from utils.path import get_project_root
from utils.error_handlers import integrityErrorPrint
from utils.dicts import map_encodings

# Convert the data into form
# match_id, round_num, t1_score, t2_score, t1_side, t2_side, t1_equip_value, t2_equip_value, equip_value_difference, map, round_winner, game_winner

project_root = get_project_root()

filepaths = [(f"{project_root}/data/raw/economy.csv", "Economies")]


def main():

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

    try:
        conn = sqlite3.connect(f"{project_root}/db/CSMatchData.db")
        cursor = conn.cursor()
        conn.row_factory = lambda cursor, row: row

        cursor.execute(sql_get_raw_round_economies)
        names = [description[0] for description in cursor.description]

        match_id_index = names.index('match_id')
        round_winner_index = names.index('round_1_winner')
        t1_start_index = names.index('t1_start')
        map_index = names.index('_map')
        t1_economies_index = names.index('round_1_t1')
        t2_economies_index = names.index('round_1_t2')
        game_winner_index = names.index('match_winner')

        print(round_winner_index, t1_start_index, map_index,
              t1_economies_index, t2_economies_index, game_winner_index)

        # row = cursor.fetchone()

        # print(row)
        print(names)
        i = 0
        for row in cursor.fetchall():

            round_count = 30 - \
                (row[round_winner_index:round_winner_index + 30]).count('')
            current_t1_wins = 0
            current_t2_wins = 0
            for round_num in range(0, round_count):

                # 0: t-side, 1: ct-side
                t1_side = 0
                t2_side = 0

                if (row[t1_start_index] == 't'):
                    if (round_num < 15):
                        t1_side = 0
                        t2_side = 1
                    else:
                        t1_side = 1
                        t2_side = 0
                else:
                    if (round_num < 15):
                        t1_side = 1
                        t2_side = 0
                    else:
                        t1_side = 0
                        t2_side = 1

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

                if not tableExists("Rounds"):
                    createTable("Rounds")

                try:
                    insert("Rounds", data)
                    # print(idx)
                    if (i % 10000 == 0):
                        print(f"{i} lines added")
                    i += 1
                except sqlite3.IntegrityError as e:
                    integrityErrorPrint(0, data, e)

                # print(data)

                if (row[round_winner_index + round_num] == 1):
                    current_t1_wins += 1
                else:
                    current_t2_wins += 1

    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
