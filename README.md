# JSON Data CRUD API



## Overview

This project is a simple FastAPI-based API for managing contacts stored in a JSON file. It provides CRUD (Create, Read, Update, Delete) operations, allowing users to interact with contact data via HTTP requests.
## Requirements

1. Python 3.7 or later
2. FastAPI
3. Tabulate
## Installation

Clone the repository:

```bash
  git clone https://github.com/Pubsch123/Contact.git
```

Navigate to the project directory:

```bash
  cd Contact
```

Create the virtual environment:

```bash
  python -m venv myenv
```
Activate the virtual environment:


for Windows: 
```bash
  source myenv/scripts/activate
```
for Unix or MacOS:
```bash
  source myenv/bin/activate
```

Install dependencies:

```bash
  pip install -r requirements.txt
```
    
## Usage

Run the FastAPI Application:

```bash
  uvicorn index:app --reload
```

Open the API documentation in your browser: 

```bash
  http://127.0.0.1:8000/docs
```

Use tools like Swagger UI to test API endpoints interactively along with that check the console for the tabulated output.
## Endpoints

`GET /data` - Retrieve all the data present in the JSON file and displayed in a tabulated format.

`GET /filter_data/{name}` - Retrieve contact information by name, displayed in a tabulated format.

`POST /insert-data` - Insert data in the JSON file along with the existing ones.

`DELETE /delete-data/{name}` - Delete data from JSON file matching the name.
## Project Structure

`index.py`: Main FastAPI application code.

`model.py`: Contain the fields present in the JSON file.

`data.json`: JSON file storing information.

`requirements.txt`: Contains the necessary packages.
## Contributing
Contributions are welcome! Feel free to open issues or pull requests for bug fixes, enhancements, or new features.
## Author

- Abhishek Kumar Tiwari (abhishek46tiwari@gmail.com)

