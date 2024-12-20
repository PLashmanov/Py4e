import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Retrieve and read the XML data
response = urllib.request.urlopen(url)
data = response.read()
print("Retrieved", len(data), "characters")

# Parse the XML data
tree = ET.fromstring(data)

# Find all <count> tags using XPath
counts = tree.findall('.//count')

# Convert text of each <count> tag to an integer and calculate the sum
numbers = [int(count.text) for count in counts]
total_sum = sum(numbers)

#data location: http://py4e-data.dr-chuck.net/comments_2085971.xml
print("Count:", len(numbers))
print("Sum:", total_sum)

