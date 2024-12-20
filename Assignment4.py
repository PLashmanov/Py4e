import urllib.request
from bs4 import BeautifulSoup

# Prompt for URL, count, and position
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("Retrieving:", url)

# Repeat the process count times
for i in range(count):
    # Fetch and parse the HTML from the URL
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    tags = soup('a')

    # Get the URL at the desired position (adjusting for 0-based index)
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

# The last URL retrieved contains the final name
last_name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment is:", last_name)
