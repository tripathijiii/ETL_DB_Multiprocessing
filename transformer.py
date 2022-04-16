import csv
import os
import pandas as pd
path = "/Users/shashwateshtripathi/Desktop/DB_Proj/Files"
path2 = "/Users/shashwateshtripathi/Desktop/DB_Proj/transformed"

def work(file_path,count,destination_path):
    f = open(file_path,"r")
    newpath = f"{destination_path}/newfile{count}.csv"
    df = pd.DataFrame(list())
    df.to_csv(newpath)
    newfile = open(newpath,"w")
    obj = csv.reader(f)
    l=[]
    print(obj)
    for rows in obj:
        rows[0]=rows[0].upper()
        rows[1]="+91"+ rows[1]
        rows[2]=rows[2].upper()
        x = float(rows[4])
        x=1.25*x
        rows[4]=x
        l.append((rows))
    obj2 = csv.writer(newfile)
    obj2.writerows(l)
    os.remove(file_path)



if __name__ == "__main__":
    count=0
    l=[]
    while(True) :
        f = open("/Users/shashwateshtripathi/Desktop/DB_Proj/communicator.txt","r")
        if os.listdir(path)==[".DS_Store"] and f.readline() == "done":

            break
        files = [x for x in os.listdir(path) if x not in l]
        for i in files:
            if(i != ".DS_Store"):
                fpath = f"{path}/{i}"
                while(os.stat(fpath).st_size<=4):
                    x=1
                work(fpath,count,path2)
                count+=1
                








