import h5py
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Carregamento dos dados
def carregar_dados():
    train_dataset = h5py.File('train_catvnoncat.h5', "r")
    test_dataset = h5py.File('test_catvnoncat.h5', "r")

    X_train = np.array(train_dataset["train_set_x"][:])
    Y_train = np.array(train_dataset["train_set_y"][:])
    X_test = np.array(test_dataset["test_set_x"][:])
    Y_test = np.array(test_dataset["test_set_y"][:])

    # Normalizar para [0,1]
    X_train = X_train / 255.
    X_test = X_test / 255.

    # Para regressão e RN rasa, achatar as imagens
    X_train_flat = X_train.reshape(X_train.shape[0], -1)
    X_test_flat = X_test.reshape(X_test.shape[0], -1)

    return X_train, Y_train, X_train_flat, X_test, Y_test, X_test_flat

# Modelos

# Regressão Logística (modelo linear)
def regressao_logistica_keras():
    model = keras.Sequential([
        layers.Input(shape=(12288,)),  # 64x64x3
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


# Rede Neural rasa (1 camada oculta)
def rn_camada_rasa_keras():
    model = keras.Sequential([
        layers.Input(shape=(12288,)),
        layers.Dense(7, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


# CNN (Rede convolucional)
def cnn_keras():
    model = keras.Sequential([
        layers.Input(shape=(64, 64, 3)),
        layers.Conv2D(16, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Execução principal
if __name__ == "__main__":
    X_train, Y_train, X_train_flat, X_test, Y_test, X_test_flat = carregar_dados()

    # epochs : Quantas vezes o modelo “vê” todo o conjunto de treino
    # batch_size : Quantos exemplos o modelo usa de cada vez antes de atualizar os pesos
    # verbose : Controla o nível de mensagens mostradas durante o treino

    # Regressão Logística
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("          Regressão Logística         ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = regressao_logistica_keras()
    model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")

    # Rede Neural de Camada Rasa
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("     Rede Neural de Camada Rasa      ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = rn_camada_rasa_keras()
    model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")

    # Rede Convolucional (CNN)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("       Rede Convolucional (CNN)       ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = cnn_keras()
    model.fit(X_train, Y_train, epochs=20, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%")