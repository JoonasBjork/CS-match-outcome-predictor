from tensorflow import keras
from keras import layers


num_of_inputs = 3


def create_model(learning_rate):

    model = keras.models.Sequential(
        [
            layers.Input(shape=(3,)),
            layers.Dense(32, activation='sigmoid'),
            layers.Dense(2),
        ]
    )

    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
                  loss=keras.losses.MeanSquaredError(),
                  metrics=[keras.metrics.MeanSquaredError(),
                           keras.metrics.Accuracy(),
                           keras.metrics.AUC()]
                  )

    return model


def train_model(model, x_train, y_train, epochs, batch_size):
    model.fit(x=x_train,
              y=y_train,
              epochs=epochs,
              batch_size=batch_size,
              verbose=1)


def test_model(model, x_test, y_test, batch_size):
    model.evaluate(
        x=x_test,
        y=y_test,
        batch_size=batch_size,
        verbose=1
    )


def save_model(model, filepath):
    model.save(filepath)


def load_model(filepath):
    return keras.models.load_model(filepath)
