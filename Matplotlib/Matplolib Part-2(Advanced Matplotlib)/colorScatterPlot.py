import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import iris


iris['Species'] = iris['Species'].replace({
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-virginica': 2
})

plt.figure(figsize=(8,6))

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['Species'])
plt.title('Scatter Plot of Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.colorbar(ticks=[0, 1, 2], label='Species')
plt.show()