import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    """Get the highs and lows from a data file"""

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)


        # Get, dates, highs, lows from this file
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data from {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get weather data from sitka.

filename = '/Users/Snapshot/PycharmProjects/data_part2/data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=5, low_index=6)

# Plot Sitka weather
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)


# Add Death Valley to Plot
filename = '/Users/Snapshot/PycharmProjects/data_part2/data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=4, low_index=5)

ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Format Plot
plt.title('Comparing the highs and lows of Sitka and death valley', fontsize=20)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(10, 130)

plt.show()