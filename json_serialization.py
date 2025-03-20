import json

def serialize_to_json(data, file_path):
    try:
        # Serialize the Python object to a JSON file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return f"Data successfully serialized to {file_path}"
    except Exception as e:
        return f"An error occurred during serialization: {e}"

def deserialize_from_json(file_path):
    try:
        # Deserialize the JSON file back to a Python object
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        return f"An error occurred during deserialization: {e}"

if __name__ == "__main__":
    # Example data to serialize
    example_data = {
        "name": "John Doe",
        "age": 30,
        "is_employee": True,
        "skills": ["Python", "Machine Learning", "Data Analysis"]
    }

    # File path for JSON
    json_file_path = "example_data.json"

    # Serialize the data
    print(serialize_to_json(example_data, json_file_path))

    # Deserialize the data
    deserialized_data = deserialize_from_json(json_file_path)
    print("Deserialized Data:", deserialized_data)
