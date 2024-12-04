import re

# Open the actual data file
file_name = "regex_sum_2085967.txt"  # Make sure to replace this with the actual path of your file
with open(file_name, 'r') as file:
    data = file.read()

# Find all numbers in the file
numbers = re.findall(r'[0-9]+', data)

# Convert the found numbers to integers
numbers = [int(num) for num in numbers]

# Compute the sum of the numbers
total_sum = sum(numbers)

# Print the total sum
print("The sum of the numbers is:", total_sum)