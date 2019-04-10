
import requests
import time   
import sys
import os
import math
import json
import pandas as pd



def print_r(data):
    with open("print.txt",'w+',encoding = 'utf-8')as f :
        f.write(str(data))

		
		
def downloadPagesOf100(numberOfPages,fileNameToWriteIn="WriteJsonToTxt.txt",state="all") : 
    """ get the issues from git api with page size  = 100 issue and  input numberOfPages as 
    number of pages u want and  into file with  filename = fileNameToWrite and state (closed or opened or all) Note that file must be json to get cvs file with it"""
    # Make a get request to get the latest position of the international space station from the opennotify api.
    jsonFormat = "String"
    PageNumber = 1
    counter = 1
    listOfJson=[]
    while (jsonFormat and PageNumber<=numberOfPages) : 
        response = requests.get("https://api.github.com/repos/tensorflow/tensorflow/issues?page="+str(PageNumber)+"&per_page=100&state="+state)
        jsonFormat = response.json()
        listOfJson+=jsonFormat
        PageNumber +=1
    with open(fileNameToWriteIn,'w+',encoding = 'utf-8')as f :
        json.dump(listOfJson, f)
    if (fileNameToWriteIn.endswith(".json")):
        df = pd.read_json(fileNameToWriteIn)
        fileNameToWriteInWithoutExtension=os.path.splitext(fileNameToWriteIn)[0]
        df.to_csv(fileNameToWriteInWithoutExtension+".csv")
def loadDataToDataFrame(jsonFileName) :
    with open('4000 issue all.json') as json_file:  
    data = json.load(json_file)
    df = pd.DataFrame(data)
    #print(df.iloc[0])
    return df;

def main() :
    #start = time. time()
    #downloadPagesOf100(40,fileNameToWriteIn="4000 issue all.json",state="all")
    #end = time. time()
    #print (end-start) 
if __name__ == "__main__":
    main()




# pd.set_option('display.max_rows', 5000)
# pd.set_option('display.max_columns', 5000)
# pd.set_option('display.width', 1000)


        
        
        

