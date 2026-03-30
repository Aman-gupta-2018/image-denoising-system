import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class Autoencoder(keras.Model):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = keras.Sequential([
            layers.Input(shape=(256, 256, 3)),
            layers.Conv2D(64, 3, activation='relu', padding='same'),
            layers.MaxPooling2D(padding='same'),
            layers.Conv2D(32, 3, activation='relu', padding='same'),
            layers.MaxPooling2D(padding='same'),
        ])
        self.decoder = keras.Sequential([
            layers.Conv2D(32, 3, activation='relu', padding='same'),
            layers.UpSampling2D(),
            layers.Conv2D(64, 3, activation='relu', padding='same'),
            layers.UpSampling2D(),
            layers.Conv2D(3, 3, activation='sigmoid', padding='same'),
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
