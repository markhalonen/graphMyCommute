import pickle
import numpy as np
import matplotlib.pyplot as plt

h2wFileName = "homeToWorkTravelTimes.p"
loadh2w = pickle.load( open(h2wFileName, "rb" ) )

w2homeFileName = "workToHomeTravelTimes.p"
loadw2h = pickle.load( open(w2homeFileName, "rb" ) )

h2wTimes = [x[1] / 60 for x in loadh2w]
h2wTimeLabels = [str(x[0].hour) + ":" + str(x[0].minute) + "am" for x in loadh2w]

w2hTimes = [x[1] / 60 for x in loadw2h]
w2hTimeLabels = [str(x[0].hour - 12) + ":" + str(x[0].minute) + "pm" for x in loadw2h]

x = np.array(h2wTimes)
y = np.array(w2hTimes)
XX, YY = np.meshgrid(x, y) #I don't really understand how this works
ZZ = XX + YY

column_labels = w2hTimeLabels
row_labels = h2wTimeLabels

data = ZZ

fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.YlOrRd)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
cbar = plt.colorbar(heatmap)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('Commute Duration (minutes)', rotation=270)
plt.xticks(rotation='vertical')
plt.xlabel("Home Departure Time")
plt.ylabel("Work Departure Time")
plt.title("Commute Duration")
plt.xlim([0,len(h2wTimeLabels)])
plt.ylim([0,len(w2hTimeLabels)])
plt.gcf().subplots_adjust(bottom=0.15)
plt.show()