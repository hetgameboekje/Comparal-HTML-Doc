import json
from bs4 import BeautifulSoup

# Initialize an empty JSON dictionary to store LI items and their counts
li_dict = {}

# Function to process an HTML document and update the JSON dictionary
def process_html_file(file_path, li_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        lis = soup.find_all('li')
        for li in lis:
            text = li.get_text()
            if text in li_dict:
                li_dict[text] += 1
            else:
                li_dict[text] = 1

# Process the first HTML document
process_html_file('modlist.html', li_dict)

# Process the second HTML document
process_html_file('modlist2.html', li_dict)

# Update counts for LI items that exist in the first document but not in the second
for li_item in li_dict.copy():  # Use copy to avoid modifying the dictionary while iterating
    if li_dict[li_item] == 1:
        li_dict[li_item] = 0

# Save the result to a JSON file
with open('li_counts.json', 'w') as json_file:
    json.dump(li_dict, json_file, indent=4)

# Print the result
print(json.dumps(li_dict, indent=4))
