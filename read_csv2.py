import os
import glob

inputPath = './'
for input_file in glob.glob(os.path.join(inputPath, "*.txt")):
    with open(input_file, 'r', newline = '') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
