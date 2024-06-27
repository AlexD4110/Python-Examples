import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a simple neural network
model = Sequential([
    Dense(32, input_shape=(784,), activation='relu'),  # Input layer
    Dense(64, activation='relu'),                      # Hidden layer
    Dense(10, activation='softmax')                    # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()
