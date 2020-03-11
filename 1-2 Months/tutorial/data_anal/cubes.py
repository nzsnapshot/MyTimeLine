import matplotlib.pyplot as plt

# Defining our data
x_values = list(range(5001))
y_values = [x**3 for x in x_values]

# Making our plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Setting our chart label and title
ax.set_title('Cubes', fontsize=15)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube of value', fontsize=12)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Setting the range of each axis
ax.axis([0, 5100, 0, 5100**3])

# Showing our plot
plt.show()

