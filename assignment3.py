import urllib.request
from bs4 import BeautifulSoup

# Prompt for URL input
url = input("Enter - ")

# Retrieve the HTML content from the URL
html = urllib.request.urlopen(url).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <span> tags
tags = soup.find_all('span', class_='comments')

# Extract numbers and compute the sum
numbers = [int(tag.text) for tag in tags]
total_sum = sum(numbers)

# Display the count and sum
print("Count:", len(numbers))
print("Sum:", total_sum)
