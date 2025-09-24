import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Simple Linear Regression Demo")

# User inputs
a = st.slider("Coefficient a", -10.0, 10.0, 2.0, 0.1)
b = st.slider("Intercept b", -10.0, 10.0, 1.0, 0.1)
noise = st.slider("Noise level", 0.0, 5.0, 1.0, 0.1)
n_points = st.slider("Number of points", 10, 500, 100, 10)

# Generate data
X = np.linspace(-5, 5, n_points)
y_true = a * X + b
y_noisy = y_true + np.random.normal(0, noise, n_points)

# Plot
fig, ax = plt.subplots()
ax.scatter(X, y_noisy, label="Noisy data")
ax.plot(X, y_true, color="red", label="True line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()

st.pyplot(fig)
