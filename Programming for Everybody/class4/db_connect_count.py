import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
# The way this command works, if the db name doesn't exist it creates it
cur = conn.cursor()
# Connecting to a DB requires two steps
# First you connect, then you send and receive commands through the cursor

cur.execute('DROP TABLE IF EXISTS Counts')
# This will get rid of the table "Counts" if it exists.

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
# Create the table "Counts" with columns "email" format required is text and "count" which
# will require an integer

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
# The stuff above we have done before, so pretty self explanitory
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
# Execute the select statement
# The "?" is used as a placeholder to be replaced by "email"
    row = cur.fetchone()
# "row" variable for fetch one table row
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
# If email not seen before, insert email address into table "Counts" and add 1 to count
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
# Or if email exists, just add 1 to the current count
    conn.commit()
# Commit changes to database

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# Select "email" and "count" from the table "Counts" order by "count" descending and limit
# to 10
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
# Print row sub 0 (email) and row sub 1 (count)

cur.close()
# Close connection to db