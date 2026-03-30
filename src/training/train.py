import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
def load_data(data_dir):
    images = []
    for filename in os.listdir(data_dir):
        img = plt.imread(os.path.join(data_dir, filename))
        images.append(img)
    return np.array(images)
def add_noise(images, noise_factor=0.5):
    noisy_images = images + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=images.shape)
    noisy_images = np.clip(noisy_images, 0., 1.)
    return noisy_images
def build_autoencoder(input_shape):
    model = models.Sequential()
    model.add(layers.Input(shape=input_shape))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2), padding='same'))
    model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 2), padding='same'))
    model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(layers.UpSampling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.UpSampling2D((2, 2)))
    model.add(layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same'))
    return model
def plot_history(history):
    plt.plot(history.history['loss'], label='train_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()  
    plt.show()

def main():
    data_dir = 'path/to/your/data'
    images = load_data(data_dir)
    noisy_images = add_noise(images)
    X_train, X_val = train_test_split(noisy_images, test_size=0.2, random_state=42)
    input_shape = images.shape[1:]  # Assuming images are of shape (width, height, channels)
    autoencoder = build_autoencoder(input_shape)
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
    history = autoencoder.fit(X_train, X_train,
                              epochs=50,
                              batch_size=128,
                              shuffle=True,
                              validation_data=(X_val, X_val))
    plot_history(history)

if __name__ == '__main__':
    main()