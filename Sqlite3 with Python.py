import sqlite3
# SQLite3 is a light-weight database which comes inbuilt with Python
conn = sqlite3.connect('emaildb.sqlite')
# Opens db file or create a new one
cur = conn.cursor()
# Gives a handle for sqlite file
# You have the full access to .db file with the handle given
# Makes sure that that TABLE is empty in beginning of execution
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts(org TEXT,count INTEGER)''')
# The above code creates a table named count with two columns
# Reads a file and stores some pattern in .db file
fname = input("Enter file name: ")
if len(fname) < 1:
    print("Enter a valid file name")
data = open(fname)
if data == None:
    print("File not found")
else:
    for line in data:
        if not line.startswith('From ') :
            continue
        pieces = line.split(' ')
        email = pieces[1].split('@')[1]
        cur.execute('''
                    SELECT count from Counts Where org = ?''',(email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''
                        INSERT into Counts values(?,1)''',(email,))
        else:
            cur.execute('''
                            UPDATE Counts set count = count+1
                            where org = ?''',(email,))

conn.commit() # Commits the changes done to database 

sqlCmd = 'SELECT org,count from Counts Order BY count DESC LIMIT 10'
for row in cur.execute(sqlCmd):
    print(row[0],row[1])
cur.close()
