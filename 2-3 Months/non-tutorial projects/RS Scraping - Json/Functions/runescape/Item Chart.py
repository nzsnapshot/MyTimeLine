import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '/Users/Snapshot/PycharmProjects/runescape/runescape/amulet - amulet.csv.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Gets dates and highs temperatures from this file
    highs, lows = [], []
    for row in reader:
        high = (row[0])
        low = int(row[1])
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, lows, c='red', alpha=0.8, linewidth=2)
plt.fill_between( highs, lows, facecolor='blue', alpha=0.5)

# Format the plot
plt.title('Amulets over 42 Players', fontsize=20)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel('Seen', fontsize= 8  )
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(rotation=45)
plt.ylim(0, 10)
plt.show()


print(highs)
