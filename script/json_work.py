import csv, json, sys, os

def save_json(json_data, fname):
    ''' Saves a json file obtained from API request to local storage.

		Parameters
		----------
		json_data : bytes
			Response object obtained from an AT API call.

        fname : string
            File save location.

		Returns
		-------

		Notes
		-----

	'''

    # decode the response from bytes to json
    json_data = json.loads(json_data.decode("utf-8"))

    # create the write file directory if there is none
    write_dir = os.path.split(fname)[0]
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)

    # save the json to file
    with open(fname, 'w', encoding = 'utf-8') as f:
        json.dump(json_data, f, indent = 2)


def json_to_csv(json_fname, csv_fname):
    ''' Writes a csv file in tidy format from a json file (unnested)

		Parameters
		----------
		json_fname : string
			File location of json file to be written to csv

        csv_fname : string
            File write location of csv.

		Returns
		-------

		Notes
		-----
        Code adapted from Gabriel Pires code here:
        https://medium.com/@gabrielpires/how-to-convert-a-json-file-to-csv-python-script-a9ff0a3f906e
	'''

    # create the write file directory if there is none
    write_dir = os.path.split(csv_fname)[0]
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)

    fileInput = json_fname
    fileOutput = csv_fname

    inputFile = open(fileInput) # open json file
    outputFile = open(fileOutput, "w", newline = "") # load csv file
    data = json.load(inputFile) # load json content
    inputFile.close() # close the input file

    output = csv.writer(outputFile) # create a csv.write

    output.writerow(data["response"][0].keys())  # write header row
    for row in data["response"]:
        output.writerow(row.values()) # write values row by row
