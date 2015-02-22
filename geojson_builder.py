import csv
import json
from geojson import Feature, FeatureCollection, GeometryCollection, dumps

msa_name = ''
county_code = 0

#key: metropolitan statistic area
#value: list with counties contained
msa_dict = {}

with open('area_definitions_m2013.csv') as definitions:
    reader = csv.DictReader(definitions)
    for row in reader:
        # new MSA
        if (row['MSA name (with MSA divisions)'] != msa_name):
            msa_name = row['MSA name (with MSA divisions)']
            county_code = row['County code']
            msa_dict[msa_name] = []
        # Add county code to allow county to be uniquely identifiable
        msa_dict[msa_name].append( (int(row['County code']), row['County name'] ))

#combining geojson objects
with open('counties_utf8.json') as data_file:
    data = json.load(data_file)

features = []

# if you are looking at this, note you have to change the names of LaPonte, IN and Dona Ana, NM
# in order for this code to parse properly
for msa, counties in msa_dict.iteritems():  #counties = (COUNTY_CODE, COUNTY_NAME)
    geometry = []
    for county in counties:
        for json_county in data['features']:
            if (int(json_county['properties']['COUNTY']) == county[0] and (json_county['properties']['NAME'] in county[1])):
                #if (not json_county['geometry'] in geometry):
                geometry.append(json_county['geometry'])
                continue
    if (len(geometry) == 0):
        print county[1] + ' in ' + msa + ' hasn\'t found matching geojson data!'
        continue    # we don't care if we miss a county or two
    geometry_collection = GeometryCollection(geometry)
    features.append(Feature(geometry=geometry_collection, properties={'NAME': msa}))

feature_collection = FeatureCollection(features)
dump = dumps(feature_collection)

with open('metropolitan_statistic_areas.json', 'w') as f:
     f.write(dump)
