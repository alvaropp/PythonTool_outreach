from glob import glob

Directories = glob("*/")

filename = "EngagementScore.dat"

EngagementScores_raw = []
for Directory in Directories:
    with open(Directory+"/"+filename) as f:
        for line in f:
            if line != "\n":
                EngagementScores_raw.append(int(line[:-1]))


EngagementScores = []

for i, Entry in enumerate(EngagementScores_raw):
    if Entry in [0, 1, 2, 3, 4]:
        EngagementScores.append(Entry)

print(EngagementScores)
print(len(EngagementScores))

import matplotlib.pyplot as plt
import numpy as np

# the histogram of the data
hist, bin_edges = np.histogram(EngagementScores, list(np.arange(-0.5, 5.5, 1)))

width = 0.7 * (bin_edges[1] - bin_edges[0])
center = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.xlabel('Engagement Score')
plt.ylabel('Number of Kids')
plt.title("Engagement Plot")
plt.axis([-0.5, 4.5, 0, 15])
plt.grid(True)
plt.bar(center, hist, align='center', width=width)
#plt.show()
plt.savefig("EnagagementPlot.pdf")
