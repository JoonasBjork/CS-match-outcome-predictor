
from pathlib import Path
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sqlite3


# Writes the training, validation and test data into model/training_data in .pkl format

def main():
    current_file = Path(__file__)
    project_root = [
        p for p in current_file.parents if p.parts[-1] == 'CSMatchData'][0]

    with sqlite3.connect(f"{project_root}/db/CSMatchData.db") as conn:

        # get data from db
        data = pd.read_sql_query("SELECT * FROM Rounds", conn)

        pd.set_option('display.max_columns', 20)
        print(data.describe())
        # sys.exit()

        # Shuffle data
        features = data.sample(frac=1).reset_index()

        labels = pd.DataFrame()

        labels['game_winner'] = features['game_winner'] - 1
        labels['round_winner'] = features['round_winner'] - 1
        # labels['match_id'] = features['match_id']

        features.drop('game_winner', inplace=True, axis=1)
        features.drop('round_winner', inplace=True, axis=1)
        # print(full_df.corr())

        # print(features)
        # print(labels)

        x_train, x_validation, y_train, y_validation = train_test_split(
            features, labels, test_size=0.4
        )

        x_validation, x_test, y_validation, y_test = train_test_split(
            x_validation, y_validation, test_size=0.5
        )

        # print(x_test.sort_index())
        # print(x_test[['t1_score', 't2_score', 'round_num']].sort_index())
        # print(y_test.sort_index())
        # print(x_train.sort_index())
        # print(y_train.sort_index())
        # print(x_validation.sort_index())
        # print(y_validation.sort_index())

        x_train = x_train[['t1_score', 't2_score', 'round_num']]
        x_validation = x_validation[['t1_score', 't2_score', 'round_num']]
        x_test = x_test[['t1_score', 't2_score', 'round_num']]

        """ dummy = x_train['round_num']

        print("-------------")

        print(dummy)
        print("-------------")

        dummy = tf.keras.utils.to_categorical(dummy)

        print(dummy)
        print("-------------") """

        data_path = f"{project_root}/src/models/training_data/"

        x_train.to_pickle(Path(data_path, 'x_train.pkl'))
        y_train.to_pickle(Path(data_path, 'y_train.pkl'))
        x_validation.to_pickle(Path(data_path, 'x_validation.pkl'))
        y_validation.to_pickle(Path(data_path, 'y_validation.pkl'))
        x_test.to_pickle(Path(data_path, 'x_test.pkl'))
        y_test.to_pickle(Path(data_path, 'y_test.pkl'))

        # print((x_train[['t1_score', 't2_score', 'round_num']],
        #        y_train,
        #        x_validation[['t1_score', 't2_score', 'round_num']],
        #        y_validation,
        #        x_test[['t1_score', 't2_score', 'round_num']],
        #        y_test))


if __name__ == "__main__":
    main()
