
import requests
import time   
import sys 
import math
def downloadPagesOf100(numberOfPages,fileNameToWriteIn="WriteJsonToTxt.txt",state="all") : 
    """ get the issues from git api with page size  = 100 issue and  input numberOfPages as number of pages u want and  into file with  filename = fileNameToWrite and state (closed or opened or all)"""
    # Make a get request to get the latest position of the international space station from the opennotify api.
    jsonFormat = "String"
    PageNumber = 1
    counter = 1
    while (jsonFormat and PageNumber<=numberOfPages) : 
        response = requests.get("https://api.github.com/repos/tensorflow/tensorflow/issues?page="+str(PageNumber)+"&per_page=100&state="+state)
        jsonFormat = response.json()
        with open(fileNameToWriteIn,'a+',encoding = 'utf-8')as f :
            for i in jsonFormat : 
                f.write("Issue number "+str(counter)+" : "+str(i)+"\n\n\n")
                counter+=1
            f.close()
            PageNumber +=1 
start = time. time()
downloadPagesOf100(30,fileNameToWriteIn="3k closed issues",state="closed")
end = time. time()
print (end-start)
