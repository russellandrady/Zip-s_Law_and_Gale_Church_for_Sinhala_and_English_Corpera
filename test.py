import json

# Read the JSON file
with open('sentences.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Get the length of the JSON array
length = len(data)

# Print the length
print("Number of sentences:", length)
