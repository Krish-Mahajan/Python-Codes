
from __future__ import print_function
import random  
import pandas as pd
import numpy as np
import warnings 
import sys  


"loading data"
def load_data(file):
    max=check_max_friends(file)
    data=pd.read_csv(file,names=[i for i in range(max)],sep=" ",header=None) 
    return data

"checking maximum friend of someone"
def check_max_friends(file):
    with open(file) as fp:
        max=0
        for line in fp:
            person=line.split(" ")
            if len(person)>max:max=len(person)
    return max   

"Making a dictionary of list of friends for every person" 
def make_graph(data):
    dict={}
    for index,row in data.iterrows(): 
        if row[0] not in dict: dict[row[0]]=[]
        for col in range(1,data.shape[1]): 
            if not pd.isnull(row[col]):
                dict[row[0]].append(row[col])
                if row[col] not in dict:
                    dict[row[col]]=[]
                dict[row[col]].append(row[0])
    return dict 

"checking if table is correct to sit for particular person"
def check_table(person,table):
        if len(tables[table])>=tableCapacity:return False
        elif (len(set(graph[person]).intersection(set(tables[table])))!=0):return False
        else:return True

"Adding table if no other table is an option"
def add_table(person):
    newtable='table'+str(random.randrange(1,1000))
    global tables
    tables[newtable]=[person]
    return 

"Adding new person in to the arrangement"
def add_person(person):
    safe=False
    for table in list(tables):       
        if check_table(person,table):
            safe=True
            tables[table].append(person)
            return
    if not safe:  
        add_table(person) 
        return 
    
"Making arrangement of all tables as prescribed"
def make_arrangement():
    for person in graph.keys(): 
        add_person(person)
    return tables 

if __name__=="__main__":
    warnings.filterwarnings('ignore')
    fileData=sys.argv[1]
    tableCapacity=int(sys.argv[2]) #Table capacity
    data=load_data(fileData)
    graph=make_graph(data)
    tables={}  
    tables["table1"]=[] #Atleast one table 'll always be required
    final = make_arrangement() #Making social network of friends
    print(len(final),end=" ") 
    for table in final: 
        print(end=" ")
        for i in  range(len(final[table])):
            print(final[table][i],end=",") 
        print('/n')



