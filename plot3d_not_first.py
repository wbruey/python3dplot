'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(10, 100, 10)
print('X linspace')
print(X)
Y = np.arange(10, 100, 10)
X, Y = np.meshgrid(X, Y)
print('X mesh')
print(X)
#Z = X*Y
Z=[
[	114	,78	,86	,53	,69	,42	,88	,55	,28],
[	43,	34,	48	,33	,42	,38,	60,	41,	27],
[	38,	33,	27,	37	,19,	12,	49	,28	,18],
[18,	25,	26,	13	,21	,22,	12	,39	,38],
[2	,7,	19,	19	,6,	13	,17,	22	,14],
[2,	10	,23	,14,	8,	5,	12,	14	,3],
[6,	12,	14	,8	,10,	5,	10,	26,	11],
[0,	1,	3,	2,	5,	3,	6,	9,	12],
[1,	0	,6	,3	,4,	1,	2,	1,	2],
]

print('Z')
print(Z)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z,rstride=1,cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 120)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.set_xlabel('% Memory Usage')
ax.set_ylabel('% CPU Usage')
ax.set_zlabel('Total Server Count')


# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
