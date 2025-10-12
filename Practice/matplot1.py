# Matplotlib : A plotting library for Python.
# Used for data visualization.
# Allows us to create line plots, bar charts, histograms, scatter plots, etc.

import matplotlib.pyplot as plt

# Line Chart
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.plot(x, y, marker="o", label="Line")
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
# plt.show()


# Bar Chart:------
categories = ["A", "B", "C"]
values = [5, 7, 3]
plt.bar(categories, values, color="skyblue")
plt.title("Bar Chart")
# plt.show()


# Pie Chart:--
sizes = [30, 20, 25, 25]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels)
plt.title("Pie Chart")
# plt.show()
