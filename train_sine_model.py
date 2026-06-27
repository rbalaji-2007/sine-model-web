import numpy as np
import tensorflow as tf
import keras

x = np.linspace(0, 2*np.pi, 500).reshape(-1, 1)
y = np.sin(x)

model = keras.models.Sequential([
    keras.layers.Dense(32, activation="tanh", input_shape=(1,)),
    keras.layers.Dense(32, activation="tanh"),
    keras.layers.Dense(1)
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss="mse"
)

print("Training the model...")

model.fit(x, y, epochs=300, verbose=0, shuffle=True)

p = (model.predict(x))

for i in range(len(x)):
        print(f"sin({x[i][0]:.2f}) = (Model) {p[i][0]:.2f} | (Actual) {np.sin(x[i][0]):.2f}")

model.save("sine_wave.keras")

print("Saved the model successfully.")
