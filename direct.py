import sqlite3
import time
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import append
connection = sqlite3.connect('test.db')

cursor = connection.execute("select* from information limit 80000000")

#connection.execute('''Create Table direct (
#    Name  Text NOT NULL,
#    Phone Text NOT NULL,
#    Gender Character(1) NOT NULL,
#    AGE INT NOT NULL,
#    Salary INT NOT NULL );''')
i=0
start=time.time()
df = pd.DataFrame(list())
df.to_csv('/Users/shashwateshtripathi/Desktop/DB_Proj/directdata.csv')
csv_file = open("/Users/shashwateshtripathi/Desktop/DB_Proj/directdata.csv","w")
csv_writer = csv.writer(csv_file, delimiter=",")
csv_writer.writerows(cursor)
connection.close()

con = sqlite3.connect('test2.db')
#con.execute('''Create Table direct (
#    Name  Text NOT NULL,
#    Phone Text NOT NULL,
#    Gender Character(1) NOT NULL,
#    AGE INT NOT NULL,
#    Salary INT NOT NULL );''')

f = open("/Users/shashwateshtripathi/Desktop/DB_Proj/directdata.csv","r")
obj = csv.reader(f)
l=[]
for rows in obj:
    rows[0]=rows[0].upper()
    rows[2]=rows[2].upper()
    x = float(rows[4])
    x=1.25*x
    rows[4]=x
    l.append(rows)
newpath = "/Users/shashwateshtripathi/Desktop/DB_Proj/transformeddirectdata.csv"
df = pd.DataFrame(list())
df.to_csv(newpath)
newfile = open(newpath,"w")
obj2 = csv.writer(newfile)
obj2.writerows(l)
newfile.close()

newfile = open("/Users/shashwateshtripathi/Desktop/DB_Proj/transformeddirectdata.csv","r")
obj2 = csv.reader(newfile)
for rows in obj2:
    con.execute("INSERT INTO direct VALUES('{}','{}','{}',{},{})".format(rows[0],'+'+rows[1],rows[2],rows[3],rows[4]))


cursor = con.execute("Select count(*) from direct")
for rows in cursor:
    print(rows)
g=(round(time.time()-start))
y=[0,g]
x=[0,10000000]
plt.plot(x,y,color='red')
plt.title('time taken for direct conversion and addition to new database table')
plt.xlabel('No. of entries')
plt.ylabel('time taken')
plt.show()
