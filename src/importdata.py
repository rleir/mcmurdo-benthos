#!/usr/bin/env python3
"""Handy utility to reformat some data for use in a nv.d3 chart."""

__author__ = "Richard Leir"
__copyright__ = "Copyright 2018, Richard Leir"
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
        years = keys[3:]

        ben_values = []
        for year in years:
            if row[year] == "":
                print("null string")
            else:
                ben_values.append( [year, row[year]])

        orgName = row['organism'] + " / "  + row['site']
        if "organism" in row:
            del row["organism"]
        if "site" in row:
            del row["site"]
        if "maxAvgAll" in row:
            del row["maxAvgAll"]

        ben_data   = {}
        ben_data["key"] = orgName
        ben_data["values"] = ben_values
        all_data.append( ben_data )
        
    # write json
    with open("chart.json", "w") as fp:
        json.dump(all_data , fp) 


