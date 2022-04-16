import csv
from multiprocessing import connection 
import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt
import time
path = "/Users/shashwateshtripathi/Desktop/DB_Proj/transformed"
connection = sqlite3.connect('test2.db')
#connection.execute('''Create Table ETL (
#    Name  Text NOT NULL,
#    Phone Text NOT NULL,
#    Gender Character(1) NOT NULL,
#    AGE INT NOT NULL,
#    Salary INT NOT NULL );''')




if __name__ == "__main__":
    l=[]
    while(True):
        d = open("/Users/shashwateshtripathi/Desktop/DB_Proj/loadercomm.txt","r")
        if os.listdir(path)==[".DS_Store"] and d.readline()=="done":
            q=open("/Users/shashwateshtripathi/Desktop/DB_Proj/communicator2.txt","r")
            g = round(time.time(),4)-float(q.readline())
            cursor = connection.execute("Select* from ETL limit 10")
            for rows in cursor:
                print(rows)
            x=[0,50000000]
            y=[0,g]
            plt.plot(x,y)
            plt.title("Multi processing 3 process for transformation")
            plt.xlabel("number of entries")
            plt.ylabel("time in sec")
            plt.show()
            break
        files = [x for x in os.listdir(path) if x not in l]
        l.extend(files)
        for i in files:
            if i!=".DS_Store":
                fpath = f"{path}/{i}"
                print(fpath)
                while(os.stat(fpath).st_size<=30000):
                    print("this worked")
                    x=1
                f = open(fpath,"r")
                obj = csv.reader(f)
                for rows in obj:
                    connection.execute("INSERT INTO ETL VALUES('{}','{}','{}',{},{})".format(rows[0],rows[1],rows[2],rows[3],rows[4]))
                os.remove(fpath)

        cursor = connection.execute("Select count(*) from ETL")
        for rows in cursor:
            print(rows)
