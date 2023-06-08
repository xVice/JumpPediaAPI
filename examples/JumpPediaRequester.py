import requests
import sys
import json
import pandas as pd

from JumpPediaWrapper import JumpPediaAPI

# Create an instance of the JumpPediaAPI
api = JumpPediaAPI(base_url='http://localhost:5000')

criteria = {}

# Check if criteria are provided in the command line
if len(sys.argv) > 1:
    # Parse the criteria from command line arguments
    for arg in sys.argv[1:]:
        key, value = arg.split('=')
        criteria[key] = value

# Call the filter_jump_levels method of JumpPediaAPI with the criteria
filtered_levels = api.filter_jump_levels(criteria)

if len(filtered_levels) > 0:
    # Export data to JSON file
    json_file_name = 'filtered_data.json'
    with open(json_file_name, 'w') as json_file:
        json.dump(filtered_levels, json_file)

    # Export data to Excel file
    excel_file_name = 'filtered_data.xlsx'
    df = pd.DataFrame(filtered_levels)
    df.to_excel(excel_file_name, index=False)

    # Export data to HTML file
    html_file_name = 'filtered_data.html'
    df.to_html(html_file_name, index=False)

    print('Data exported successfully to:', json_file_name, ',', excel_file_name, ' and ', html_file_name)
else:
    print('No results found based on the provided criteria.')