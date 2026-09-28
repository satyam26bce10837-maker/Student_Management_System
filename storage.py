import json

# Load data from a JSON file
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    return data

# Save data to a JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)