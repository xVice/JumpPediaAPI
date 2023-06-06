# Example script
This script is an example of using the requests library and tabulate library to send a POST request to an API endpoint and display the filtered data in a table format. Here's a small usage example for this script:

Suppose you have a local API running at http://localhost:5000/api/jumps, which provides information about different levels of jumps. The API accepts criteria for filtering the levels. You want to filter the levels based on their difficulty and style.

To use the script, open your terminal or command prompt and navigate to the directory where the script is located. Then, you can run the script with the desired criteria as command line arguments.

For example, to filter the levels with difficulty 'Intermediate' and location 'Metro Kingdom', you can run the script like this:
```py
python JumpPediaRequester.py diff="7/10" location="Metro Kingdom"
```
The script will send a POST request to the API endpoint with the provided criteria as a JSON payload. It will then retrieve the filtered data from the response and display it in a table format using the tabulate library.

If the request is successful and the response status code is 200, the script will save the filtered data to filtered_data.json, filtered_data.xlsx and filtered_data.html for simple viewing. If any error occurs during the request, it will print an error message along with the error text from the response.

Please note that for this script to work, you need to have the requests, pandas and openpyxl librarys installed in your Python environment. You can install them using the following commands:
```
pip install requests
pip install pandas
pip install openpyxl
```