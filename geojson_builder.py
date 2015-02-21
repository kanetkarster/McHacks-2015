import csv
import json
from geojson import Feature, Point, FeatureCollection

with open('counties_utf8.json') as data_file:
    data = json.load(data_file)

msa_name = ''
with open('area_definitions_m2013.csv') as definitions:
    reader = csv.DictReader(definitions)
    for row in reader:
        if (row['MSA name (with MSA divisions)'] != msa_name):
            msa_name = row['MSA name (with MSA divisions)']
            print msa_name
