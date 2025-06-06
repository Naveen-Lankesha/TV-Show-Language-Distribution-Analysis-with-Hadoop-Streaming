#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)  # skip header
for row in reader:
    try:
        lang = row[4]  # dataset's column
        print(f"{lang}\t1")
    except IndexError:
        continue