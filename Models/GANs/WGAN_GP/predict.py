import keras
import numpy as np
import cv2

model = keras.models.load_model("/home/republic/Documents/Ganadev/Sonar/Outputs/GANs/WGAN/Results1/model/generator.h5", compile=False)

while True:
    noise = np.random.normal(0, 1, (1, model.input_shape[1]))
    generated_image = model.predict(noise, verbose=False) * 127.5 + 127.5
    generated_image = generated_image[..., ::-1].astype(np.uint8)
    cv2.imshow("Generated Image", generated_image[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()