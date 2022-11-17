from train_model import load_model, test_model
from pathlib import Path
import numpy as np
import pandas as pd
import tensorflow as tf
import math


def main():

    current_file = Path(__file__)
    project_root = [
        p for p in current_file.parents if p.parts[-1] == 'CSMatchData'][0]

    model = load_model(
        f"{project_root}/src/models/saved_models/my_model.model")

    # config = model.get_config()
    # print(config)

    data_path = f"{project_root}/src/models/training_data/"
    x_test = pd.read_pickle(Path(data_path, 'x_test.pkl'))
    y_test = pd.read_pickle(Path(data_path, 'y_test.pkl'))
    # print(x_test.shape)
    # print(y_test.shape)

    # print(x_test.head(5))
    # print(y_test.head(5))

    # print(np.array(y_test.head(5)))

    # predictions = np.around(model.predict(x_test))

    # print(predictions)
    test_model(model, x_test, y_test, 32)
    output = tf.keras.Lambda(lambda x: round(x))(model.output)

    # prediction = model.predict(x_test.head(25))
    # arr = np.array(y_test.head(25))
    # for i in range(25):
    #     print(f"Prediction: {prediction[i]}, Solution: {arr[i]}")

    # print(y_test[0])


if __name__ == '__main__':
    main()
