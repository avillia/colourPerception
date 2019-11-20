import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from tkinter import *


colourSet = []

for r in range(0, 31, 5): # creating dataset with MinMaxNormalized values
    for g in range(0, 31, 5):
        for b in range(0, 31, 5):
            colourSet.append((r/256, g/256, b/256))

for r in range(45, 256, 15):
    for g in range(49, 256, 19):
        for b in range(54, 256, 23):
            colourSet.append((r/256, g/256, b/256))


def square_array(array):
    N = round(len(array)**0.5)
    return [array[i:i + N] for i in range(0, N*N, N)]


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
                cluster[i] = "#{:02X}{:02X}{:02X}".format(int(cluster[i][0]*256),
                                                          int(cluster[i][1]*256),
                                                          int(cluster[i][2]*256))

        height = int(700/(number+1))
        startHeightIndent = 30
        for i in range(len(clusters)):
            width = bool(len(clusters[i]) < 1300)
            for j in range(len(clusters[i])):
                    canvas.create_rectangle(j+30 if width else j+5, (i*30)+startHeightIndent, j+40 if width else j+6, (i*30)+startHeightIndent+height,
                                            width=0, fill=clusters[i][j])
            startHeightIndent += height


        root.mainloop()
