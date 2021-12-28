import csv

csvfile = open("colorSet.csv", "w", newline="")

writer = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for rgb in range(0, 40, 2):
    writer.writerow((rgb, rgb, rgb))

for r in range(45, 256, 15):
    for g in range(55, 256, 25):
        for b in range(58, 256, 28):
            writer.writerow((r, g, b))

for rgb in range(216, 256, 2):
    writer.writerow((rgb, rgb, rgb))
