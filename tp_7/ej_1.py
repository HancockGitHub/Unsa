import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100000)
y1 = (x**2-1)/(x**3+1)
y2 = (x+1)/(x+2)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
