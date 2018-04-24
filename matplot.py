# beginnining from: https://www.labri.fr/perso/nrougier/teaching/matplotlib/scripts/grid_ex.py
# try out of visualisation with matplotlib
# TO DO: try to find out how to fill between two points

import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()

# set title
plt.title('Map of houses\nAccording to model with 20 houses')

# set x and y axis
ax.set_xlim(0,15)
ax.set_ylim(0,17)

# refers to small and bigg squares
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

# set labels for x and y xaxis and color
plt.xlabel('Length of map')
plt.ylabel('Width of map')
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('r')

# sets style for small and big squares
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

# set labels
ax.set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
ax.set_yticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])


plt.show()
