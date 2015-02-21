import csv
import json
from geojson import Feature, Point, FeatureCollection

with open('counties_utf8.json') as data_file:
    data = json.load(data_file)

msa_name = ''
county_code = 0

#key: metropolitan statistic area
#value: list with counties contained
counties = {}

with open('area_definitions_m2013.csv') as definitions:
    reader = csv.DictReader(definitions)
    for row in reader:
        if (row['MSA name (with MSA divisions)'] != msa_name):
            msa_name = row['MSA name (with MSA divisions)']
            county_code = row['County code']
            counties[msa_name] = []
        counties[msa_name].append((row['County code'], row['County name'].rsplit(' ')[0]))
