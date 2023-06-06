import requests
import sys
from tabulate import tabulate

# API endpoint URL
url = 'http://localhost:5000/api/jumps'

criteria = {}

# Check if criteria are provided in the command line
if len(sys.argv) > 1:
    # Parse the criteria from command line arguments
    for arg in sys.argv[1:]:
        key, value = arg.split('=')
        criteria[key] = value

# Send a POST request to the API endpoint with the criteria as JSON payload
response = requests.post(url, json=criteria)

# Check the response status code
if response.status_code == 200:
    # Retrieve the filtered data from the response
    filtered_data = response.json()

    if len(filtered_data) > 0:
        # Format the data in a table
        table = []
        headers = filtered_data[0].keys()
        for level in filtered_data:
            table.append(list(level.values()))

        # Print the table
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print('No results found based on the provided criteria.')
else:
    print('Error occurred:', response.text)
