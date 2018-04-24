import matplotlib.pyplot as plt
import numpy as np
# function that populates x or y
x = [1, 2, 3]
y = [5, 7, 4]

plt.plot(x, y, label='First Line')
plt.xlabel('Length of map')
plt.ylabel('Width of map')
plt.legend(loc='best')

# afmetingen grid x = 320 x y = 360
plt.grid()


plt.title('Map of houses\nAccording to model with 20 houses')
plt.show()
