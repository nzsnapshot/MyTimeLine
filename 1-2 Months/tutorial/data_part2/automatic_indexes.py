import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Filenames
filename = '/Users/Snapshot/PycharmProjects/data_part2/data/sitka_weather_2018_simple.csv'
filename = '/Users/Snapshot/PycharmProjects/data_part2/data/death_valley_2018_simple.csv'
place_name = ''

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Get date, highs and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
        # Grab the station name if not already set.
        if not place_name:
            place_name = row[name_index]
            print(place_name)

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Plot the low and high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Format the Plot
plt.title('Temperatures for 2018', fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


