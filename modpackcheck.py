import json
from bs4 import BeautifulSoup

# Initialize dictionaries to store LI items and their counts for both documents
document1_li = {}
document2_li = {}
document1 = input("What is the filename in this folder for the previous version? \n")
document2 = input("What is the filename in this folder for the upcoming version? \n")
# Function to process an HTML document and update the dictionaries
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
process_html_file(document1, document1_li)

# Process the second HTML document
process_html_file(document2, document2_li)

# Initialize the final dictionary with LI items and their counts
li_dict = {}

# Update counts for lines present in both documents
for item in document1_li:
    if item in document2_li:
        li_dict[item] = 2
        del document2_li[item]
    else:
        li_dict[item] = 1

# Add lines present only in the second document
for item in document2_li:
    li_dict[item] = 0

# Save the result to a JSON file
with open('li_counts.json', 'w') as json_file:
    json.dump(li_dict, json_file, indent=4)

# Print the result
print(json.dumps(li_dict, indent=4))
