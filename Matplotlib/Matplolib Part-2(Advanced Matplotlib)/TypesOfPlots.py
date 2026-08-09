import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from DataM import iplBallByBall

# Scatter plots 

# plt.scatter(batter['avg'], batter['strike_rate'])
# plt.title('Scatter Plot of Batsman Performance')
# plt.xlabel('Average Runs')
# plt.ylabel('Strike Rate')
# plt.show()


# # 3D Scatter Plot
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# pts = ax.scatter(batter['avg'], batter['strike_rate'], batter['runs'], c=batter['runs'], cmap='viridis')
# ax.set_xlabel('Average Runs')
# ax.set_ylabel('Strike Rate')
# ax.set_zlabel('Runs')
# plt.show()


#3D Line Plots

# x=[10,8,0]
# y=[7,1,0]
# z=[10,0,16]

# fig = plt.figure()
# ax=fig.add_subplot(111, projection='3d')
# ax.scatter(x,y,z)
# ax.plot(x,y,z,color='red',label='Line Plot')
# plt.show()


# # 3D Surface Plots (f(x)=x^2+y^2)

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)

# X, Y = np.meshgrid(x, y)

# Z = X**2 + Y**2

# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111, projection='3d')

# p=ax.plot_surface(X, Y, Z, cmap='viridis')
# fig.colorbar(p)

# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# ax.set_title("3D Surface Plot")

# plt.show()


# Contour Plots

# fig = plt.figure(figsize=(8,6))
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# X, Y = np.meshgrid(x, y)
# Z = X**2 + Y**2
# C=plt.contour(X, Y, Z, levels=20)
# fig.colorbar(C)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Contour Plot")
# plt.show()


# filled contour plot


# plt.contourf(X, Y, Z, levels=20, cmap='viridis')
# plt.show()




# Heatmaps
tempdf=iplBallByBall[(iplBallByBall['ballnumber'].isin([1,2,3,4,5,6])) & (iplBallByBall['batsman_run']==6)]

grid=tempdf.pivot_table(index='overs', columns='ballnumber', values='batsman_run', aggfunc='count')

# plt.figure(figsize=(8,6))
# sns.heatmap(grid, annot=True, fmt='d', cmap='YlGnBu')
# plt.title("Heatmap of Batsman Runs by Overs and Ball Number")
# plt.xlabel("Ball Number")
# plt.ylabel("Overs")
# plt.show()





