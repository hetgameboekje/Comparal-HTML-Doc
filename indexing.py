import json

# Read the JSON file
with open('li_counts.json', 'r') as json_file:
    li_dict = json.load(json_file)

# Set the index variable
index = input("Already added: 2 \n Newly added: 1 \n Removed : 0 \n")

# Print lines with a count of 1 when index is 1
if index.isdigit(): 
    indexInt = int(index)
    if indexInt == 1:
        for item, count in li_dict.items():
            if count == 1:
                print(f'{item}')
    if indexInt == 2:
        for item, count in li_dict.items():
            if count == 2:
                print(f'{item}')
    if indexInt == 0:
        for item, count in li_dict.items():
            if count == 0:
                print(f'{item}')
else:
    print("\n this is not a digit!")
