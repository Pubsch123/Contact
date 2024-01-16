from fastapi import FastAPI, HTTPException
import json
from tabulate import tabulate
from model import Contact

app = FastAPI()


# This is the name of the JSON file that is used in this project
json_file_path = 'data.json'


# This function read the file and filter the data whose name matches the given name
def filter_json_by_name(json_data, name):
    filtered_data = [item for item in json_data if item.get('name') == name]
    return filtered_data

# This function read the file
def read_json_data(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    

# This function writes the new data into the json File along with the existing ones
def write_json_data(json_file_path, new_data):
    existing_data = read_json_data(json_file_path)
    existing_data.extend(new_data)

    with open(json_file_path, 'w') as file:
        json.dump(existing_data, file, indent=2)

# This function overwrites the new data into the json file
def write_json_data_for_delete(json_file_path, data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)



@app.get("/data")
def display_all_data():
    # Read data from the JSON file
    data = read_json_data(json_file_path)

    # Check if there is any data
    if not data:
        print("No data found.")
        return

    # Display data in a tabulated format
    headers = data[0].keys()
    table_data = [[row[header] for header in headers] for row in data]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))


@app.get("/filter_data/{name}")
async def get_data(name: str):
    try:
        # Specify the path to your JSON file
        json_file_path = 'data.json'

        # Read JSON data
        json_data = read_json_data(json_file_path)

        # Filter JSON data by Name
        filtered_result = filter_json_by_name(json_data, name)

        # Check if there is any data
        if not filtered_result:
            return f"No data found for name: {name}"

        # Convert filtered data to SQL-like table format using tabulate
        table = tabulate(filtered_result, headers="keys", tablefmt="pretty")

        # To print the output on the console.
        print(table)

        return table
    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {str(e)}")
        # Raise HTTP 500 with a generic error message
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/insert-data",response_model=Contact)
async def enter_data(contact:Contact):
    try:
        # Convert Pydantic model to dictionary
        json_data = contact.dict()

        # Specify the path to your JSON file
        json_file_path = 'data.json'

        # Insert the data into the JSON file
        write_json_data(json_file_path, [json_data])

        return json_data
    
    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {str(e)}")
        # Raise HTTP 500 with a generic error message
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.delete("/delete-data/{name}", response_model=dict)
async def delete_data(name: str):
    # Specify the path to your JSON file
    json_file_path = 'data.json'

    # Read existing data
    existing_data = read_json_data(json_file_path)

    # Find the index of the contact with the specified name
    index_to_delete = next((i for i, c in enumerate(existing_data) if c["name"].strip() == name.strip()), None)

    if index_to_delete is None:
        # Print debug information
        print(f"Contact not found for name: {name}")
        raise HTTPException(status_code=404, detail="Contact not found")

    # Delete the contact from the list
    deleted_contact = existing_data.pop(index_to_delete)

    # Write the updated data back to the JSON file
    write_json_data_for_delete(json_file_path, existing_data)

    # Return a message indicating the deleted contact
    return {"message": f"Contact {name} deleted", "deleted_contact": deleted_contact}







