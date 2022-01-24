#Name: Joseph Bobowski
#Date: 1/24/2022

import matplotlib.pyplot as dataPlot

squares = [1,4,9,16,25]

#fig - variable that represents the figure of the plot
#ax - variable that represents a single plot
fig, ax = dataPlot.subplots()
ax.plot(squares)

dataPlot.show()