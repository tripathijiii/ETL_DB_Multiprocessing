import sqlite3

connection = sqlite3.connect('test.db')
for i in range(10000000):
    connection.execute("INSERT INTO information VALUES('shashwatesh','7908019448','m',22,25000)")
    connection.execute("INSERT INTO information VALUES('ranjit','7908019448','m',23,22000)")
    connection.execute("INSERT INTO information VALUES('uday','7908019448','m',24,21000)")
    connection.execute("INSERT INTO information VALUES('ram bahadur','7908019448','f',22,24000)")
    connection.execute("INSERT INTO information VALUES('optimus','7908019448','m',21,25002)")

cursor = connection.execute("select count(*) from information")
for row in cursor:
    print(row)
connection.commit()
