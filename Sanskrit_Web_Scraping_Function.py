def San_text(j):
    
    import requests
    import pandas as pd
    import re
    values = []
    from bs4 import BeautifulSoup as soup
    url = [
        'http://newssanskrit.blogspot.com/2018/10/',
        'http://newssanskrit.blogspot.com/2018/11/',
        'http://newssanskrit.blogspot.com/2018/12/',
        'http://newssanskrit.blogspot.com/2019/01/',
        'http://newssanskrit.blogspot.com/2019/02/',
        'http://newssanskrit.blogspot.com/2019/03/',
        'http://newssanskrit.blogspot.com/2019/04/',
        'http://newssanskrit.blogspot.com/2019/05/',
        'http://newssanskrit.blogspot.com/2019/06/',
        'http://newssanskrit.blogspot.com/2019/07/',
        'http://newssanskrit.blogspot.com/2019/08/',
        'http://newssanskrit.blogspot.com/2019/09/',
        'http://newssanskrit.blogspot.com/2019/10/',
        'http://newssanskrit.blogspot.com/2019/11/',
        'http://newssanskrit.blogspot.com/2019/12/',
        'http://newssanskrit.blogspot.com/2020/01/',
        'http://newssanskrit.blogspot.com/2020/02/',
        'http://newssanskrit.blogspot.com/2019/03/'
          ]
    for i in range(len(url)):
    
        data = requests.get(url[i])
    
        html = soup(data.text, 'html.parser')
        values += [div.text.strip() for div in html.find_all('div', { 'class': 'post-body entry-content'},{'style':'text-align:center'})]
    l1 = []
    l2 = []
    data = []
    title = []
    body = []
    df = pd.DataFrame()
    for i in range(len(values)):
    
        data = re.findall(r".*", values[i])
        while("" in data) : 
            data.remove("")
        if len(data)>=2:
            l1 = data[0]
            l2 = data[1:]
        title += [l1];
        body += [l2];
    df=pd.DataFrame(list(zip(title, body)), columns =['title', 'body'])

    df['title']=df["title"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)
    df['body']=df["body"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)
    df['body'][2]
    #j=30000

    for i in range(len(df)):
        title = df['title'][i]
        body = df['body'][i]+'\n'
        filename = '/home/ravi/Desktop/IIT BHU/Sanskrit_Web_Scraping_2/Function_output/'+str(j)+'.trec.txt'
        file = open(filename, 'w')
        file.write("<DOC>\n")
        file.write("<DOCNO>")
        file.write(str(j))
        j=j+1
        file.write("<\DOCNO>\n")
        file.write("<HEAD>")
        file.write(title)
        file.write("<\HEAD>\n")
        file.write("<BODY>\n")
        file.write(body)
        file.write("<\BODY>\n")
        file.write("<\DOC>\n")
        file.close()
