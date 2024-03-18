import matplotlib.pyplot as plt
import numpy as np

# Data for the first graph
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

# Data for the second graph
x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2)

# Create a figure with two subplots
fig, ax= plt.subplots(1, figsize=(6,6))

# Plot the first graph on the first subplot
ax.plot(x1, y1, label='sin(x)', color='blue')
ax.set_title('Sine Function')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.legend()

plt.pause(1)
ax.clear

# Plot the second graph on the second subplot
ax.plot(x2, y2, label='cos(x)', color='red')
ax.set_title('Cosine Function')
ax.set_xlabel('x')
ax.set_ylabel('cos(x)')
ax.legend()

# Adjust the layout
plt.tight_layout()

# Show the plots
plt.show()
