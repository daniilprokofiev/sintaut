import json

# JSON array representing a list of fruits
fruits_json = '["apple", "banana", "orange"]'

# Parse the JSON array
fruits = json.loads(fruits_json)

# Print the list of fruits
print(fruits)
