import sqlite3

# Create an in-memory SQLite database and table
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create the Ages table
cursor.execute("""
CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
)
""")

# Insert the provided data into the table
data = [
    ('Hari', 35),
    ('Anya', 18),
    ('Ghyll', 15),
    ('Silas', 35),
    ('Jaxon', 35),
    ('Anousha', 25)
]

cursor.executemany("INSERT INTO Ages (name, age) VALUES (?, ?)", data)

# Run the SQL query to get the hex result
cursor.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
result = cursor.fetchall()

# Close the connection
connection.close()

# Print the first result in the console
print(result[0][0])
