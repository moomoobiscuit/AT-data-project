"""
Function to convert a json file into a csv file

Code adapted from Gabriel Pires code here:
https://medium.com/@gabrielpires/how-to-convert-a-json-file-to-csv-python-script-a9ff0a3f906e
"""

import csv, json, sys, os
# check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:

    # create the write file directory if there is none
    write_path = os.path.split(sys.argv[2])[0]
    if not os.path.exists(write_path):
        os.makedirs(write_path)

    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput) # open json file
    outputFile = open(fileOutput, "w", newline = "") # load csv file
    data = json.load(inputFile) # load json content
    inputFile.close() # close the input file
    output = csv.writer(outputFile) # create a csv.write
    output.writerow(data["response"][0].keys())  # header row
    for row in data["response"]:
        output.writerow(row.values()) # values row


# consider changing the structure of the json from the source download to only include response
# then we don't have to do the dictionary stuff here