import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 300

firstPerson = np.array([8.5, 0.5, 3.0, 1.0, 1.5, 3.0, 6.5]) / 0.24
secondPerson = np.array([9.5, 1.0, 2.0, 1.5, 0.5, 2.5, 7.0]) / 0.24
thirdPerson = np.array([7.0, 1.5, 1.0, 2.5, 2.0, 2.0, 8.0]) / 0.24

xPositions = np.array(list(range(0,14,2)))
firstPositions = xPositions - 0.5
secondPositions = xPositions
thirdPositions = xPositions + 0.5

xTicks = ["Work", "Family", "Homeworks", "Individual", "Socializing", "Spare Time", "Sleeping"]
plt.xticks(xPositions, xTicks, rotation = "vertical")
plt.title("Daily Time Distribution")
plt.ylabel("Time Spend Percentage (%)")
plt.xlabel("Activities")
plt.axes().yaxis.grid(linestyle = "--")

plt.bar(firstPositions, firstPerson, 0.5, color = "r")
plt.bar(secondPositions, secondPerson, 0.5, color = "b")
plt.bar(thirdPositions, thirdPerson, 0.5, color = "g")
plt.legend(["Charles", "Henry", "Susan"])
plt.show()