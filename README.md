# FocalLengthStatistics

The script helps you understand what focal lengths you use the most. Especially useful if you use a variable focal length lens and want to know what focal lengths are most important to you.

The script will read the metadata for all the JPG files inside the target directory and calculate the statistics for the usage of different focal lengths.

## Prerequisites

* `python 3.6` or above
* `exifread`

Install all the requirements inside `requirements.txt`. You can do that by running `python -m pip install -r requirements.txt` or `runme.sh` if on linux.

## Usage

The script accepts 3 arguments.

* `-p` or `--path` - the path to the folder containing all the JPEGs you want to generate statistics for
* `--hist` - boolean argument, if present a histogram of all the focal lengths will be display
* `b` or `--bin_size` - the size of the bin for the histogram

You can also get this information using `-h`.
