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

def chart_by_year():
    input_file = 'four_org.csv'

    output_file = 'chart_by_year.json'
    all_data   = []

    # read input
    with open(input_file, newline='') as csvfile:

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
        
    # write output
    with open(output_file, "w") as fp:
        json.dump(all_data , fp) 


def chart_by_site(year):
    input_file = 'three_sites_' + year + '.csv'

    output_file = 'chart_by_site_' + year + '.json'
    all_data   = []

    # read input
    with open(input_file, newline='') as csvfile:

        input_data = csv.DictReader(csvfile)
        for row in input_data:
            #build data struc
            keys = list(row.keys())
            sites = keys[1:]

            organism_counts = []
            site_num = 0
            for site in sites:
                site_num += 1
                if row[site] == "":
                    organism_counts.append( [site_num, "Number.NaN"])
                else:
                    organism_counts.append( [site_num, row[site]])

            organism_name = row['organism']
            organism_data   = {}
            organism_data["key"] = organism_name
            organism_data["values"] = organism_counts
            all_data.append( organism_data )
            
    # write output
    with open(output_file, "w") as fp:
        json.dump(all_data , fp) 


if __name__ == "__main__":
    # execute only if run as a script
    chart_by_year()

#    years_with_complete_data=['1988', '2002', '2003', '2004', '2007', '2008', '2009', '2010', '2011']
    years_with_complete_data=['2009', '2010', '2011']
    for year in years_with_complete_data:
        chart_by_site(year)
