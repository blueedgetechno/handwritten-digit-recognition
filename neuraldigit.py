# %% imports
from tensorflow import keras
import numpy as np
import os
import matplotlib.pyplot as plt

# %% load dataset
digit_mnist = keras.datasets.mnist
(train_images, train_labels), (test_images,
                               test_labels) = digit_mnist.load_data()

class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# %% preprocessing
train_images = train_images / 255.0

test_images = test_images / 255.0

# %% model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# %% compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# %% train
model.fit(train_images, train_labels, batch_size=128, epochs=5,
          verbose=1, validation_data=(test_images, test_labels))

# %% testing
load = 0
if(load):
    model = keras.models.load_model('./keras_mnist.h5')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1)
print('Test accuracy:', test_acc)

# %% saving
save = 0
if save:
    save_dir = "./"
    model_name = 'keras_mnist.h5'
    model_path = os.path.join(save_dir, model_name)
    model.save(model_path)
# %% prediction

predictions = model.predict(test_images)
plt.figure()
print("Predicted :", class_names[np.argmax(predictions[0])])
plt.imshow(test_images[0], cmap='gray', interpolation='none')
plt.grid(False)
plt.show()
