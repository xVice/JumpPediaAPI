# JumpPediaAPI Documentation
This is a Flask-based API for managing and retrieving jump level data. It provides endpoints to retrieve all jump levels and filter levels based on specific criteria.

## Installation
To install and run the API, follow these steps:
- Clone the repository or download and unzip the repo and open it in a shell/cmd: 
```bash
git clone <repository_url>
```

- Navigate to the project directory: 
```bash
cd <project_directory>
```

- Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```

- Activate the virtual environment:

   On Windows:
   ```
   venv\Scripts\activate
   ```

   For macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
 
- Install the required dependencies:
```
pip install -r requirements.txt
```
 
- Start the api
```
python JumpPediaAPI.py
```
 
The API will start running on http://localhost:5000.
 
## API Endpoints
 
Retrieve All Jump Levels
- URL: /api/jumps
- Method: GET
- Description: Retrieves all jump levels.
- Response: Returns a JSON array containing information about each jump level.

Filter Jump Levels
- URL: /api/jumps
- Method: POST
- Description: Filters jump levels based on specific criteria.
- Request Body: The request body should be a JSON object containing the filter criteria. The keys should correspond to the field names of the Level model.
- Response: Returns a JSON array containing the filtered jump levels.

## Updating the Dataset
The API provides functionality to update the dataset from a remote source ([JumpPedia-URL](https://raw.githubusercontent.com/JoniKauf2/Jumpedia/main/data/jump_data.json)). To update the dataset, you can run the following command:
```
python JumpPediaAPI.py updatedataset
```
This command will fetch the data from the remote source, parse it, and store it in the jump_data.db SQLite database.

## Repopulating the Database
If you want to repopulate the database with the existing dataset, you can run the following command:
```
python JumpPediaAPI.py repopulate
```
This command will drop the existing tables, create new ones, and populate them with data from the jump_data.json file.

Note: Make sure you have the jump_data.json file in the project directory before running this command.

You can also chain the commands:
```
python JumpPediaAPI.py updatedataset repopulate
```
