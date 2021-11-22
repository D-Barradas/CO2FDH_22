import os
## Create the json file from the csv file

def create_jsonfile(csv_file, json_file):
    """
    Create a json file from a csv file
    """
    import json
    import csv
    data ={}
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            accesion = row["Accesion"]
            data[accesion] = row
    with open(json_file, 'w') as json_file:
        json_file.write( json.dumps(data, indent=4) ) 

create_jsonfile("/Users/barradd/Documents/BARRADD_Things/CO2FDH_22/files/blast_output_desc.csv", "/Users/barradd/Documents/BARRADD_Things/CO2FDH_22/files/blast_output_desc.json")