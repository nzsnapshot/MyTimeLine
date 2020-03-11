import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Edited CSV file for combat levels sorted
filename_csv = '/Users/Snapshot/PycharmProjects/runescape/runescape/yeet.csv'
with open(filename_csv) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    combat_index = header_row.index('COMBAT')
    seen_index = header_row.index('SEEN')

    # Get the combat and times seen
    combat_ge, seen_ge = [], []
    for row in reader:
        comb = int(row[combat_index])
        see = int(row[seen_index])
        combat_ge.append(comb)
        seen_ge.append(see)

y_pos = combat_ge
x_pos = seen_ge

#####################COLOURS###############################
    # clist = [(0, "red"), (0.125, "red"), (0.25, "orange"), (0.5, "green"),
    #          (0.7, "green"), (0.75, "blue"), (1, "blue")]
    # rvb = mcolors.LinearSegmentedColormap.from_list("", clist)
    # N = 60
    # x = np.arange(N).astype(float)
    # y = np.random.uniform(0, 5, size=(N,))
    #####################COLOURS###############################

# Formatting the bar chart
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 9))
ax.bar(y_pos, x_pos,color= rvb(x/N))
plt.title('Combat levels from 20,000 Runescape players')
plt.ylabel('Times Seen', fontsize=12)
plt.xlabel('Combat Levels', fontsize=12)
plt_ticks= np.arange(np.min(0),np.max(126)+0.001,5.0)
plt.xticks(plt_ticks , rotation=-45)
plt.tick_params( labelsize=8)

plt.show()














