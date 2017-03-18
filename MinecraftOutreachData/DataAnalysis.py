from glob import glob

Directories = glob("./SED/*")

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
    else:
        EngagementScores.append(5)

print(EngagementScores)
print(len(EngagementScores))

import matplotlib.pyplot as plt
import numpy as np

# The histogram of the data
hist, bin_edges = np.histogram(EngagementScores, list(np.arange(-0.5, 6.5, 1)))
print(hist)
print(bin_edges)

width = 0.7 * (bin_edges[1] - bin_edges[0])
center = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.xlabel('Engagement Score')
plt.ylabel('Number of Kids')
plt.title("Engagement Plot")
plt.axis([-0.5, 5.5, 0, 15])
plt.grid(True)
plt.bar(center, hist, align='center', width=width)
labels = ['0', '1', '2', '3', '4', 'NA']
plt.xticks(center, labels)
plt.savefig("EnagagementPlot.pdf")
