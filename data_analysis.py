import sqlite3
from queries.sql_analysis import *


def main():
    conn = sqlite3.connect("db/CSMatchData.db")
    cursor = conn.cursor()

    print("Probability that the team with the higher rank wins:")
    res = cursor.execute(better_rank_wins)
    data = res.fetchone()
    print(f"{data[0] / data[1] * 100} %")

    # TODO: Find compartments with similar probabilities limited to some maximum probability.
    # Ranges with close to half win probabilities can be used to minimize the effect of skill
    # difference as a factor in the data.
    print("Probability that the team with the higher rank wins when similarly ranked teams:")
    for i in range(4, 10):
        inputs = {"min_rank": 3, "max_rank": i}
        res = cursor.execute(incremented_better_rank_wins, inputs)
        data = res.fetchone()
        print(f"{data[0] / data[1] * 100} %")

    conn.close()


if __name__ == "__main__":
    main()
