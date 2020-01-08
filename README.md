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

#### Example usage
`python focal_length_statistics.py -p . --hist -b 5`

## Output
Running the script for a collection of 1909 photos prints the following to the console:

```
651 photos at 55.0 mm
446 photos at 18.0 mm
124 photos at 12.0 mm
62 photos at 40.7 mm
56 photos at 35.8 mm
41 photos at 31.5 mm
38 photos at 25.4 mm
36 photos at 39.0 mm
34 photos at 34.3 mm
32 photos at 26.5 mm
32 photos at 37.4 mm
32 photos at 48.4 mm
31 photos at 24.3 mm
29 photos at 46.3 mm
25 photos at 30.2 mm
24 photos at 32.9 mm
22 photos at 18.8 mm
21 photos at 22.3 mm
21 photos at 23.3 mm
21 photos at 19.6 mm
20 photos at 28.9 mm
20 photos at 27.7 mm
19 photos at 20.5 mm
19 photos at 44.4 mm
16 photos at 42.5 mm
14 photos at 50.5 mm
13 photos at 21.4 mm
10 photos at 52.7 mm
```
The list is ordered by the number of photos at the given focal length.

### The histogram
