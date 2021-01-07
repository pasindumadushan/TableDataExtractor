import sqlite3

with sqlite3.connect("AttendenceSheet.db") as db:
    cursor = db.cursor()


cursor.execute('''
DROP TABLE sheet;
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sheet(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
StudentNo VARCHAR(20) NOT NULL,
Title VARCHAR(20) NOT NULL,
StudentName VARCHAR(40) NOT NULL,
Signature VARCHAR(20) NOT NULL);
''')
