import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import batsman



#2D line plot

# plotting a simple grapgh

price=[65000,70000,45000,35000,85000,90000,4540000]
year=[2015,2016,2017,2018,2019,2020,2021]

# plt.plot(year,price)
# plt.show()



# now from dataframe
# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.show()


# plotting multiple lines in a single graph
# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.plot(batsman['index'],batsman['RG Sharma'])
# plt.show()


# labels and title
# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.plot(batsman['index'],batsman['RG Sharma'])
# plt.xlabel('Years')
# plt.ylabel('Runs')
# plt.title('Runs scored by Kohli and Sharma')
# plt.legend(['V Kohli','RG Sharma'])
# plt.show()


# colors(hex) and line(width and style) and marker(size)

# plt.plot(batsman['index'],batsman['V Kohli'],color='#FF5733',linewidth=2,linestyle='--',marker='o',markersize=5)
# plt.show()


# limmiting axis

plt.plot(year,price)
# plt.xlim(2015,2021)
plt.ylim(30000,1000000)
plt.grid()
plt.show()