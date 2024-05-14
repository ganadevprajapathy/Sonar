import tensorflow as tf
from keras import layers

# Define the generator model
def build_generator(noise_dim, img_shape):
    inputs = layers.Input(shape=noise_dim, name="input")

    # Modified Dense layer with new output size
    x = layers.Dense(25 * 128 * 256, use_bias=False)(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    # Reshape to match the new dense layer output
    x = layers.Reshape((25, 128, 256))(x)
    assert x.shape == (None, 25, 128, 256)

    x = layers.Conv2D(128, (5, 5), strides=(1, 1), padding='same', use_bias=False)(x)
    assert x.shape == (None, 25, 128, 128)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    x = layers.UpSampling2D(size=(2, 2))(x)
    x = layers.Conv2D(64, (5, 5), strides=(1, 1), padding='same', use_bias=False)(x)
    assert x.shape == (None, 50, 256, 64)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    x = layers.UpSampling2D(size=(2, 2))(x)
    x = layers.Conv2D(1, (5, 5), strides=(1, 1), padding='same', use_bias=False)(x)

    # Add tanh activation
    x = layers.Activation('tanh')(x)
    assert x.shape == (None, img_shape[0], img_shape[1], 1)

    model = tf.keras.Model(inputs=inputs, outputs=x)

    return model


# Define the discriminator model
def build_discriminator(img_shape):
    inputs = layers.Input(shape=img_shape, name="input")

    x = layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same')(inputs)
    x = layers.LeakyReLU(0.2)(x)

    x = layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same')(x)
    x = layers.LeakyReLU(0.2)(x)

    x = layers.Flatten()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.Model(inputs=inputs, outputs=x)

    return model