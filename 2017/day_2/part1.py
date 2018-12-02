#!/usr/bin/python3
import numpy
import sys

input_file = sys.argv[1]

data = numpy.genfromtxt(input_file, delimiter='\t')
diffs = []

# part 1
for row in data:
    max_row = numpy.max(row)
    min_row = numpy.min(row)
    diffs.append(max_row - min_row)

print("Answer part 1: {0}".format(int(numpy.sum(diffs))))

# part 2
length = len(data[0])
summed = []
for row in data:
    for index, column in enumerate(row):
        for subindex, digit in enumerate(row):
            if index != subindex:
                if column % digit == 0:
                    print("{0} % {1} = {2}".format(column, digit, column % digit))
                    summed.append(int(int(column) / int(digit)))

print("Answer part 2: {0}".format(sum(summed)))


