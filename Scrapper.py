#Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
url = 'https://covid19.assam.gov.in/'
page = requests.get(url, headers = header)

#Creating a soup object
soup = BeautifulSoup(page.content, 'html.parser')

#Finding the table which contain the data
table = soup.find('tbody')
#print(table.prettify())

#Creating a list to store the data
productlist=[]

#Iterating through the table
for item in table.find_all('tr'):
    dic = {}
    index= item.find('h6')
    _index = index.get_text() 
    dic['Details'] = _index
    #print(index.get_text())
  
    value = item.find('small', class_ = 'text-muted')
    #Cleaning the data
    _value = value.get_text().replace('Cases in Assam', " ").strip()
    dic['Figures'] = _value
    productlist.append(dic)

#Converting to a pandas dataframe
df=pd.DataFrame(productlist)

#Printing the dataframe
print(df)