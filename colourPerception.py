import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from tkinter import *


colourSet = []

for rgb in range(0, 40, 2):
    colourSet.append((rgb / 256, rgb / 256, rgb / 256))

for r in range(45, 256, 15):
    for g in range(55, 256, 25):
        for b in range(58, 256, 28):
            colourSet.append((r/256, g/256, b/256))

for rgb in range(216, 256, 2):
    colourSet.append((rgb / 256, rgb / 256, rgb / 256))



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

        height = int(700/(number+2))
        startHeightIndent = 30
        for i in range(len(clusters)):
            width = bool(len(clusters[i]) < 1300)
            for j in range(len(clusters[i])):
                    canvas.create_rectangle(j+30 if width else j+5, (i*int(height/7))+startHeightIndent, j+40 if width else j+6, (i*int(height/7))+startHeightIndent+height,
                                            width=0, fill=clusters[i][j])
            startHeightIndent += height


        root.mainloop()
