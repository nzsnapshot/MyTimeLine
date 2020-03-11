import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks whilst the programme is active
while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points of the Random Walk
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

    # Emphasize the first and last pointsn
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
