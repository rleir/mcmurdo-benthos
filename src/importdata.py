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

input_file = 'four_org.csv'

# read csv
with open(input_file, newline='') as csvfile:

    all_data   = []
    input_data = csv.DictReader(csvfile)
    for row in input_data:
        #build data struc
        keys = list(row.keys())
        years = keys[3:]

        organism_counts = []
        for year in years:
            if row[year] == "":
                organism_counts.append( [year, "Number.NaN"])
            else:
                organism_counts.append( [year, row[year]])

        organism_name_and_site = row['organism'] + " / "  + row['site']
        if "organism" in row:
            del row["organism"]
        if "site" in row:
            del row["site"]
        if "maxAvgAll" in row:
            del row["maxAvgAll"]

        organism_data   = {}
        organism_data["key"] = organism_name_and_site
        organism_data["values"] = organism_counts
        all_data.append( organism_data )
        
    # write json
    with open("chart.json", "w") as fp:
        json.dump(all_data , fp) 


