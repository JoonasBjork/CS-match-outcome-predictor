from train_model import create_model, train_model, test_model, save_model
import pandas as pd
from pathlib import Path
import numpy as np
# import tensorflow as tf

LEARNING_RATE = 0.1
BATCH_SIZE = 32
EPOCHS = 1


def main():
    current_file = Path(__file__)
    project_root = [
        p for p in current_file.parents if p.parts[-1] == 'CSMatchData'][0]

    # print(project_root)

    data_path = f"{project_root}/src/models/training_data/"
    # print(data_path)

    x_train = pd.read_pickle(Path(data_path, 'x_train.pkl'))
    y_train = pd.read_pickle(Path(data_path, 'y_train.pkl'))
    x_validation = pd.read_pickle(Path(data_path, 'x_validation.pkl'))
    y_validation = pd.read_pickle(Path(data_path, 'y_validation.pkl'))

    model = create_model(LEARNING_RATE)
    # print(model.summary())

    train_model(model, x_train, y_train, EPOCHS, BATCH_SIZE)

    test_model(model, x_validation, y_validation, BATCH_SIZE)

    save_model(model, f"{project_root}/src/models/saved_models/my_model.model")


if __name__ != "__name__":
    main()
