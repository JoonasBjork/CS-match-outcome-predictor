
from pathlib import Path
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder
import sqlite3
import sys


# Writes the training, validation and test data into model/training_data in .pkl format

def main():
    current_file = Path(__file__)
    project_root = [
        p for p in current_file.parents if p.parts[-1] == 'CSMatchData'][0]

    with sqlite3.connect(f"{project_root}/db/CSMatchData.db") as conn:

        # get filtered data from db
        data = pd.read_sql_query("SELECT * FROM Rounds", conn)

        # pd.set_option('display.max_columns', 20)
        # print(data.describe())
        # print(data.corr())
        # sys.exit()

        # Shuffle data
        raw_data = data.sample(frac=1).reset_index()

        labels = pd.DataFrame()

        # labels['game_winner'] = raw_data['game_winner'] - 1
        labels['round_winner'] = raw_data['round_winner'] - 1
        # labels['match_id'] = raw_data['match_id']

        raw_data.drop('game_winner', inplace=True, axis=1)
        raw_data.drop('round_winner', inplace=True, axis=1)
        # print(full_df.corr())

        # print(raw_data)
        # print(labels)

        x_train, x_validation, y_train, y_validation = train_test_split(
            raw_data, labels, test_size=0.4
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

        # feature_labels = ['t1_score', 't2_score', 'map']
        # feature_labels = ['t1_equip_value', 't2_equip_value']
        feature_labels = ['t1_score', 't2_score',
                          't1_equip_value', 't2_equip_value']
        x_train = x_train[feature_labels]
        x_validation = x_validation[feature_labels]
        x_test = x_test[feature_labels]

        # One hot encode all columns in 'columns'
        # columns = ['round_num']
        # x_train = pd.get_dummies(x_train, columns=columns)
        # x_validation = pd.get_dummies(x_validation, columns=columns)
        # x_test = pd.get_dummies(x_test, columns=columns)

        # print(x_train.head(10))

        # dummy = tf.keras.utils.to_categorical(dummy)

        data_path = f"{project_root}/src/models/training_data/"

        x_train.to_pickle(Path(data_path, 'x_train.pkl'))
        y_train.to_pickle(Path(data_path, 'y_train.pkl'))
        x_validation.to_pickle(Path(data_path, 'x_validation.pkl'))
        y_validation.to_pickle(Path(data_path, 'y_validation.pkl'))
        x_test.to_pickle(Path(data_path, 'x_test.pkl'))
        y_test.to_pickle(Path(data_path, 'y_test.pkl'))


if __name__ == "__main__":
    main()
