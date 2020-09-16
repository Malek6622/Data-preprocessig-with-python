#importing the packages
from xml.etree.ElementTree import parse
import numpy as np 
import pandas as pd 
import math
import requests

#the url from wich we'll get the infos
url = "http://www.torontopolice.on.ca/newsreleases/rss.php"
#downloading the data and storing it in a file (feed.xml)
r = requests.get(url)
with open('feed.xml', 'wb') as file:
    file.write(response.content)
document = parse('feed.xml')
xroot = document.getroot() 

title = []
link = []
author = []
pubDate = []
description = []
#getting the infos we need from the XML file (title,link...) and putting them in a list
for i in document.iter('item'):
        title.append(i.findtext('title'))
        link.append(i.findtext('link'))
        author.append(i.findtext('author'))
        pubDate.append(i.findtext('pubDate'))
        description.append(i.findtext('description'))
#creating a dictionnary with the data so we can have the name of the column and the data
df = pd.DataFrame({'title': title,'link': link ,'published': pubDate,'author': author,'description':description})
#splitting the <title> with the ',' delimiter 
df['event'], df["A"], df["B"], df["C"]= df["title"].str.split(",", 3).str
#copying the data to keep it unchange
df['1']=df['A'].copy()
df['2']=df['B'].copy()
df['3']=df['C'].copy()
#only keeping columns whete values aren't numeric
df['1'] = df['1'].mask(pd.to_numeric(df['1'], errors='coerce').notna())
df['2'] = df['2'].mask(pd.to_numeric(df['2'], errors='coerce').notna())
df['3'] = df['3'].mask(pd.to_numeric(df['3'], errors='coerce').notna())
#copying the data to keep it unchange
df['1']=df['A'].copy()
df['2']=df['B'].copy()
df['3']=df['C'].copy()
#only keeping columns whete ther's more than 2 whitespaces 
df["1"].loc[df['1'].str.count(" ")==2]= math.nan
df["2"].loc[df['2'].str.count(" ")==2]= math.nan
df["3"].loc[df['3'].str.count(" ")==2]= math.nan
#merging the three columns into one 
df['place'] = (df['1'].fillna('') + df['2'].fillna(''))+ df['3'].fillna('')
#droping the columns we  don't needd anymore
df = df.drop(['1','2','3'], axis= 1)
#copying the data to keep it unchange
df['1']=df['A'].copy()
df['2']=df['B'].copy()
df['3']=df['C'].copy()
#only keeping columns whete values aren't numeric
df['1'] = df['1'].mask(pd.to_numeric(df['1'], errors='coerce').notna())
df['2'] = df['2'].mask(pd.to_numeric(df['2'], errors='coerce').notna())
df['3'] = df['3'].mask(pd.to_numeric(df['3'], errors='coerce').notna())
##only keeping columns whete ther's more than 2 whitespaces 
df["1"].loc[df['1'].str.count(" ")>2]= math.nan
df["2"].loc[df['2'].str.count(" ")>2]= math.nan
df["3"].loc[df['3'].str.count(" ")>2]= math.nan
#merging the three columns into one 
df['name'] = (df['1'].fillna('') + df['2'].fillna(''))+ df['3'].fillna('')
#droping the columns we  don't needd anymore
df = df.drop(['A','B','C','1','2','3'], axis= 1)
#looking for the lat and asingning the to a column called lat
df['lat'] = df['description'].apply(lambda st:st[st.find("@43.")+1:st.find(",-")])
#looking for the long and asingning the to a column called long
df['long'] = df['description'].apply(lambda st:st[st.find(",-")+1:st.find("z/")])
df['long'] = df['long'].apply(lambda st:st[st.find(",-")+1:st.find("t/")])
df
