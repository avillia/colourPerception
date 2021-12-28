from tkinter import Tk, Canvas

from matplotlib import pyplot
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering

from readers import ColourList, read_dataset

def dendrogram(colours: ColourList):
    pyplot.figure(figsize=(12, 12))
    pyplot.title("Dendrograms")

    hierarchy.dendrogram(hierarchy.linkage(colours, method="ward"))

    pyplot.show()


def perform_clustering(number: int, colours: ColourList):
    clustering = AgglomerativeClustering(
        n_clusters=number,
        affinity="euclidean",
        linkage="ward",
    )
    return clustering.fit_predict(colours)


def build_colorgram(number: int, colours: ColourList):
    """
    Build a decent-looking colored strips representing set of colours
    described by a separate term
    :param number:
    :param colours:
    :return:
    """
    clusters = perform_clustering(number, colours)
    root = Tk()
    root.attributes("-fullscreen", True)
    canvas = Canvas(root, width=1400, height=840, bg="white")
    canvas.pack()

    clusters = list(zip(clusters, colours))
    result = [
        [elem[1] for elem in filter(lambda a: a[0] == num, clusters)]
        for num in {duo[0] for duo in clusters}
    ]

    clusters = result
    for cluster in result:
        for i, elem in enumerate(cluster):
            cluster[i] = f"#{int(elem[0]):02X}{int(elem[1]):02X}{int(elem[2]):02X}"

    height = int(700 / (number + 2))
    startHeightIndent = 30
    for i, cluster in enumerate(clusters):
        width = len(cluster) < 1300
        for j, elem in enumerate(cluster):
            canvas.create_rectangle(
                j + 30 if width else j + 5,
                (i * int(height / 7)) + startHeightIndent,
                j + 40 if width else j + 6,
                (i * int(height / 7)) + startHeightIndent + height,
                width=0,
                fill=elem,
            )
        startHeightIndent += height

    root.mainloop()


def main(load_dataset_from: str):
    colours = read_dataset(load_dataset_from)
    dendrogram(colours)
    for i in range(2, 8):
        build_colorgram(i, colours)


if __name__ == "__main__":
    main("colorSet.csv")
