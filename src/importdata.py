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

    all_data   = []
    benreader = csv.DictReader(csvfile)
    for row in benreader:
        #build data struc
        keys = list(row.keys())
        years = keys[2:]

        ben_values = []
        for year in years:
            ben_values.append( [year, row[year]])

        orgName = row['organism']
        if "organism" in row:
            del row["organism"]
        if "maxAvg" in row:
            del row["maxAvg"]

        ben_data   = {}
        ben_data["key"] = orgName
        ben_data["values"] = ben_values
        all_data.append( ben_data )
        
    # write json
    with open("chart.json", "w") as fp:
        json.dump(all_data , fp) 


