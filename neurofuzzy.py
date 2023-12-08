import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(units=64, activation='relu', input_shape=(2,)), 
    keras.layers.Dense(units=1)  
])


model.compile(optimizer='adam', loss='mean_squared_error')

inputs = np.array([[angle_value, angular_velocity_value] for _ in range(num_samples)])
outputs = np.array([output_value for _ in range(num_samples)])

model.fit(inputs, outputs, epochs=10)

neuro_fuzzy_output = model.predict(np.array([[some_angle_value, some_angular_velocity_value]]))
print(neuro_fuzzy_output)
