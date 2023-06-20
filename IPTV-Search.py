import csv
import requests

# Define the URL of the IPTV database CSV file
url = 'https://github.com/iptv-org/database/raw/master/data/channels.csv'

# Function to search for links based on a keyword
def search_links(keyword):
    # Send a GET request to retrieve the CSV file
    response = requests.get(url)
    response.raise_for_status()

    # Create a CSV reader for the response content
    reader = csv.reader(response.text.strip().split('\n'))

    # Extract the header row
    headers = next(reader)

    # Find the indices of relevant columns
    name_column_index = headers.index('name')
    language_column_index = headers.index('languages')
    categories_column_index = headers.index('categories')
    is_nsfw_column_index = headers.index('is_nsfw')
    website_column_index = headers.index('website')

    # Create a dictionary to store unique channel information
    unique_channels = {}

    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the keyword is present in the name column
        if keyword.lower() in row[name_column_index].lower():
            # Retrieve the relevant information from the row
            name = row[name_column_index].strip()
            language = row[language_column_index].strip()
            categories = row[categories_column_index].strip()
            is_nsfw = row[is_nsfw_column_index].strip()
            website = row[website_column_index].strip()

            # Add the information to the unique channels dictionary
            unique_channels[website] = {
                'name': name,
                'language': language,
                'categories': categories,
                'is_nsfw': is_nsfw
            }

    # Print the unique channel information
    for website, info in unique_channels.items():
        print('Name:', info['name'])
        print('Language:', info['language'])
        print('Categories:', info['categories'])
        print('Is NSFW:', info['is_nsfw'])
        print('Website:', website)
        print()

# Prompt the user to enter a search keyword
keyword = input('Enter a keyword to search for: ')
print("\n")

# Perform the search and filter out repeated results
search_links(keyword)

