#Import requirements.
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup as soup
#request.get() method used to get all data inside the url
data = requests.get('http://newssanskrit.blogspot.com/2020/03/')
#html.parser used to break the input in some tokens and responsible for constrcuting the parse tree by analyzing the docoment structure according to language syntex rules, with help of BeautifulSoup.
html = soup(data.text, 'html.parser')
#Extracting required text with applying for loop on 'html' variable on the basis of some spacial tags, class and style.
values = [div.text.strip() for div in html.find_all('div', { 'class': 'post-body entry-content'},{'style':'text-align:center'})]

#Creating empty lists and DataFrame. 
l1 = []
l2 = []
data = []
title = []
body = []
df = pd.DataFrame()
#Applying for loop on 'values' list 
for i in range(len(values)):
    #Finding data by applying reguler expression on 'values' list. 
    data = re.findall(r".*", values[i])
    #Applying while loop on 'data' list for removing blank items.
    while("" in data) : 
        data.remove("")
    #Use if condition on 'data' list for checking and storing 'data' lists data in 'l1' and 'l2' on the basis of certain condation.
    if len(data)>=2:
        l1 = data[0]
        l2 = data[1:]
    #append list 'l1' into list 'title' and list 'l2' into list 'body'.
    title += [l1];
    body += [l2];
#list 'title' add in dataframes 'title' column and 'body' into 'body' column.
df=pd.DataFrame(list(zip(title, body)), columns =['title', 'body'])
#remove squire brackets from dataframes columns.
df['title']=df["title"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)
df['body']=df["body"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)


j=30000
#loop for apply these write commands on all rows of dataframe to make .txt files .
for i in range(len(df)):
    #'title' and 'body' variables assign inside loop for every file.
    title = df['title'][i]
    body = df['body'][i]+'\n'
    #file name and file path to store file at specific location.
    filename = '/home/ravi/Desktop/IIT BHU/Sanskrit_Web_Scraping_2/text/'+str(j)+'.trec.txt'
    #open file to write text inside file.
    file = open(filename, 'w')
    #write '<Doc>' tag .
    file.write("<DOC>\n")
    #write '<DocNo>' tag .
    file.write("<DOCNO>")
    #write Document no .
    file.write(str(j))
    #incrementin variable 'j' for changing file name and document no.
    j=j+1
    #write '<\DocNo>' tag .
    file.write("<\DOCNO>\n")
    #write '<HEAD> tag .
    file.write("<HEAD>")
    #write 'title' of file inside '<HEAD> tag . 
    file.write(title)
    #write '<\HEAD>' tag .
    file.write("<\HEAD>\n")
    #write '<BODY>' tag .
    file.write("<BODY>\n")
    #write 'body' of file inside '<BODY>' tag .
    file.write(body)
    #Write '<\BODY> tag .
    file.write("<\BODY>\n")
    #write '<\DOC> tag . 
    file.write("<\DOC>\n")
    #close and save the written file .
    file.close()
