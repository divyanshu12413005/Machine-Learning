import matplotlib.pyplot as plt
import numpy as np

# plotting 2D graphs
# x=y

x=np.linspace(-10,10,100)
y=x
# plt.plot(x,y)


# y=x^2

# y=x**2

# y=sin(x)


# y=np.sin(x)

# y=xlog(x)

y=x*np.log(x)


plt.plot(x,y)
plt.show()

