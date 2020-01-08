#!/home/thalvadzhiev/anaconda3/bin/python
import exifread
import os
import re
from collections import Counter 
import sys
from optparse import OptionParser
import matplotlib.pyplot as plt

# options parser
parser = OptionParser()
parser.add_option("-p", "--path", dest="path",
                  help="the path to the folder containing the JPGs")

parser.add_option("--hist",
                  action="store_true", dest="histogram", default=False,
                  help="Show histogram")
parser.add_option("-b", "--bin_size",
                  action="store", dest="bin_size", type="int", default=5,
                  help="The bin size for the histogram")

(options, args) = parser.parse_args()
start = time.time()
##### end of options parser

if not options.path:
    parser.error('Path to folder containing JPEGs not given.')

focal_length_tag = "EXIF FocalLength"



folder_path = options.path

focal_lengths = []
jpgs_in_directory = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]

if len(jpgs_in_directory) == 0:
    parser.error(f"The given directory ({options.path}) does not contain any JPGs")

for i, file_name in enumerate(jpgs_in_directory):
    print("\r {}/{}".format(i + 1, len(jpgs_in_directory)), end="")
    
    with open(folder_path + "/" + file_name, "rb") as f:
        tags = exifread.process_file(f)
        focal_ratio = tags[focal_length_tag].values[0]
        focal_lengths.append(focal_ratio.num / focal_ratio.den)
end = time.time()

max_focal_length = max(focal_lengths)
min_focal_length = min(focal_lengths)
interval_focal_lengths = max_focal_length - min_focal_length

n_bins = int(interval_focal_lengths // options.bin_size)

print("\r There are {} JPGs".format(len(jpgs_in_directory)))
print("The 10 most common focal lengths are:\n")

c = Counter(focal_lengths)
most_common = c.most_common(10)
for el in most_common:
    print("{} photos at {} mm".format(el[1], el[0]))

if options.histogram:
    plt.hist(focal_lengths, bins=n_bins, rwidth=0.7)
    plt.show()


