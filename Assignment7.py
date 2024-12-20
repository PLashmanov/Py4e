import urllib.request
import urllib.parse
import json

# Base URL for the API
api_url = "http://py4e-data.dr-chuck.net/opengeo?"

# Prompt for the location
location = input("Enter location: ")

# URL encode the query parameters
params = {'q': location}
url = api_url + urllib.parse.urlencode(params)

print("Retrieving", url)

# Retrieve the JSON data from the API
response = urllib.request.urlopen(url)
data = response.read().decode()  # Decode to convert bytes to string
print("Retrieved", len(data), "characters")

# Parse the JSON data
try:
    info = json.loads(data)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
    exit()

# Debug: Print the entire JSON response
print(json.dumps(info, indent=2))

#Location: Arizona State University
#Not sure why it doesn't print the plus code, but it can be found in the json
# Extract the plus_code
try:
    plus_code = info['plus_code']['global_code']
    print("Plus code:", plus_code)
except KeyError:
    print("KeyError: The expected 'plus_code' field was not found in the JSON response.")
