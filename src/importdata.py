#!/usr/bin/env python3
"""Handy utility to reformat some data for use in a d3 chart."""

__author__ = "Richard Leir"
__copyright__ = "Copyrighte 2018, Richard Leir"
__credits__ = ["Kathy Conlan", "Mike Bostock"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Richard Leir"
__email__ = "rleir at leirtech ddot com"
__status__ = "Production"

import csv
import json

# read csv
with open('benthos.csv', newline='') as csvfile:
#    firstRowLabels=""

    ben_data = {}
    benreader = csv.DictReader(csvfile)
    for row in benreader:
#        print(row['1988per'], row['2004per'])
        orgName = row['organism']
        #build data struc
        keys = list(row.keys())
        years = keys[2:]
        for year in years:
            print(year)
        if "organism" in row:
            del row["organism"]
        if "maxAvg" in row:
            del row["maxAvg"]

        ben_data[orgName] = row
        
    # write json
    with open("chart.json", "w") as fp:
        json.dump(ben_data , fp) 


