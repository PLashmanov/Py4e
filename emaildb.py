import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Create the table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open and read the mbox.txt file
filename = input('Enter file name: ')
if len(filename) < 1: filename = 'mbox.txt'
with open(filename, 'r') as file:
    for line in file:
        if not line.startswith('From: '): continue
        # Extract the domain/organization
        email = line.split()[1]
        org = email.split('@')[1]

        # Update the database
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit all changes to the database
conn.commit()

# Print the top 10 organizations by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print('Top 10 organizations:')
for row in cur.execute(sqlstr):
    print(f'{row[0]}: {row[1]}')

# Close the database connection
cur.close()
