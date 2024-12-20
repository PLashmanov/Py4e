import urllib.request
import json

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Retrieve and read the JSON data
response = urllib.request.urlopen(url)
data = response.read().decode()  # Decode to convert bytes to string
print("Retrieved", len(data), "characters")

# Parse JSON data
info = json.loads(data)

# Extract comment counts and compute the sum
counts = [item['count'] for item in info['comments']]
total_sum = sum(counts)

#location : http://py4e-data.dr-chuck.net/comments_2085972.json

# Output results
print("Count:", len(counts))
print("Sum:", total_sum)
