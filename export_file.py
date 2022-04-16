import sqlite3,csv
import pandas as pd
import subprocess
import os
import time

filer = open("/Users/shashwateshtripathi/Desktop/DB_Proj/communicator2.txt","w")
filer.write(str(round(time.time(),4)))

con = sqlite3.connect('test.db')
i=0
k=0
f = open("/Users/shashwateshtripathi/Desktop/DB_Proj/communicator.txt","r+")
f.truncate(0)
f.close()
while i<=100000000:
    #try:
    cursor = con.execute("Select* from information limit {} offset {}".format(1000000,i))
    df = pd.DataFrame(list())
    df.to_csv('/Users/shashwateshtripathi/Desktop/DB_Proj/Files/data{}.csv'.format(k))
    csv_file = open("/Users/shashwateshtripathi/Desktop/DB_Proj/Files/data{}.csv".format(k),"w")
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerows(cursor)
    if k==2:
        subprocess.Popen("python3 multi_transformer.py",shell = True)
    k+=1
    i+=1000001
    #except:
    #    print("error occured")
    #    break

f = open("/Users/shashwateshtripathi/Desktop/DB_Proj/communicator.txt","w")
f.write("done")
f.close()