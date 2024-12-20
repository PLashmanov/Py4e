import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Create the tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
handle = open('tracks.csv')

# Parse and insert data
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 6: continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    genre = pieces[3]  # Extract genre information
    rating = pieces[4]
    length = pieces[5]

    # Insert Artist
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert Genre
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert Album
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # Insert Track
    cur.execute('''
        INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, album_id, genre_id, length, rating, 1))

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()

