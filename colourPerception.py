import csv
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from tkinter import *


def dendrogram():
    plt.figure(figsize=(12, 12))
    plt.title("Dendrograms")

    dend = shc.dendrogram(shc.linkage(colourSet, method='ward'))
    plt.show()


def show_colours(number):
    clustering = AgglomerativeClustering(n_clusters=number, affinity='euclidean', linkage='ward')
    clusters = clustering.fit_predict(colourSet)

    root = Tk()
    root.attributes("-fullscreen", True)
    canvas = Canvas(root, width=1400, height=840, bg='white')
    canvas.pack()

    clusters = list(zip(clusters, colourSet))
    result = []
    for num in set([duo[0] for duo in clusters]):
        result.append([elem[1] for elem in filter(lambda a: a[0] == num, clusters)])

    clusters = result
    for cluster in result:
        for i in range(len(cluster)):
            cluster[i] = "#{:02X}{:02X}{:02X}".format(int(cluster[i][0] * 256),
                                                      int(cluster[i][1] * 256),
                                                      int(cluster[i][2] * 256))

    height = int(700 / (number + 2))
    startHeightIndent = 30
    for i in range(len(clusters)):
        width = bool(len(clusters[i]) < 1300)
        for j in range(len(clusters[i])):
            canvas.create_rectangle(j + 30 if width else j + 5, (i * int(height / 7)) + startHeightIndent,
                                    j + 40 if width else j + 6, (i * int(height / 7)) + startHeightIndent + height,
                                    width=0, fill=clusters[i][j])
        startHeightIndent += height

    root.mainloop()


colourSet = []
reader = csv.reader(open("colorSet.csv", "r", newline=""), delimiter=' ', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    colourSet.append(row)
