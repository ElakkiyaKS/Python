import tensorflow as tf
import numpy as np
# Define the XOR input data
x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_train = np.array([[0], [1], [1], [0]], dtype=np.float32)
# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, input_dim=2, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Train the model
model.fit(x_train, y_train, epochs=1000, verbose=0)
# Evaluate the model
loss, accuracy = model.evaluate(x_train, y_train)
print(f"Loss: {loss}, Accuracy: {accuracy}")
# Make predictions
predictions = model.predict(x_train)
rounded_predictions = np.round(predictions)
print(f"Predictions: {rounded_predictions}")
