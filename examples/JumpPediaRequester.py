import requests
import sys
import json
import pandas as pd

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
        # Export data to JSON file
        json_file_name = 'filtered_data.json'
        with open(json_file_name, 'w') as json_file:
            json.dump(filtered_data, json_file)

        # Export data to Excel file
        excel_file_name = 'filtered_data.xlsx'
        df = pd.DataFrame(filtered_data)
        df.to_excel(excel_file_name, index=False)

        # Export data to HTML file
        html_file_name = 'filtered_data.html'
        df.to_html(html_file_name, index=False)

        print('Data exported successfully to:', json_file_name, ',', excel_file_name, ' and ', html_file_name)
    else:
        print('No results found based on the provided criteria.')
else:
    print('Error occurred:', response.text)