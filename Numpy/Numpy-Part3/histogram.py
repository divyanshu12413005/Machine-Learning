import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1, 100, 20)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(a)

print(np.histogram(a, bins=bins))  # return the histogram of the elements with 10 bins

plt.hist(a, bins=bins, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value range")
plt.ylabel("Frequency")
plt.show()
