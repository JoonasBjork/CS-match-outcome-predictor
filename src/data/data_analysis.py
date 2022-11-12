import sqlite3
from queries.sql_analysis import *
from utils.path import get_project_root

project_root = get_project_root()


def main():
    try:
        conn = sqlite3.connect(f"{project_root}/db/CSMatchData.db")
        cursor = conn.cursor()

        print("Probability that the team with the higher rank wins:")
        res = cursor.execute(sql_better_rank_wins)
        data = res.fetchone()
        print(f"{data[0] / data[1] * 100} %")

        # TODO: Find compartments with similar probabilities limited to some maximum probability.
        # Ranges with close to half win probabilities can be used to minimize the effect of skill
        # difference as a factor in the data.

        # might be unneeded because the data could be balanced
        print("Probability that the team with the higher rank wins when similarly ranked teams:")
        low = 3
        high = 4
        for i in range(4, 10):
            inputs = {"min_rank": 3, "max_rank": i}
            res = cursor.execute(sql_incremented_better_rank_wins, inputs)
            data = res.fetchone()
            print(f"{data[0] / data[1] * 100} %")

        table_max_rank = cursor.execute(sql_max_rank).fetchone()[0]
        print("Winrates of all ranks")
        for i in range(1, table_max_rank + 1):
            inputs = {"rank": i}
            res = cursor.execute(sql_single_rank_wins_and_losses, inputs)
            data = res.fetchone()
            if (data[1] != 0):
                print(f"{data[0] / (data[0] + data[1]) * 100} %")
            else:
                if (data[0] == 0):
                    print("No matches")
                else:
                    print("100 %")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
