from model_functions import load_model, test_model
from pathlib import Path
import pandas as pd


def main():

    current_file = Path(__file__)
    project_root = [
        p for p in current_file.parents if p.parts[-1] == 'CSMatchData'][0]

    model = load_model(
        f"{project_root}/src/models/saved_models/my_model.model")

    print("Model weights")
    for layer in model.layers:
        print(layer.get_config(), layer.get_weights())
    # print(model.get_weight_paths())

    # config = model.get_config()
    # print(config)

    data_path = f"{project_root}/src/models/training_data/"
    x_test = pd.read_pickle(Path(data_path, 'x_test.pkl'))
    y_test = pd.read_pickle(Path(data_path, 'y_test.pkl'))

    # print(np.array(y_test.head(5)))

    # predictions = np.around(model.predict(x_test))

    # print(predictions)
    print("Model main test with test data")
    test_model(model, x_test, y_test, 32)
    # prediction = model.predict(x_test.head(25))
    # arr = np.array(y_test.head(25))
    # for i in range(25):
    #     print(f"Prediction: {prediction[i]}, Solution: {arr[i]}")

    # print(y_test[0])


if __name__ == '__main__':
    main()
