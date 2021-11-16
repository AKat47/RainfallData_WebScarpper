from pandas.core.indexes.datetimes import date_range
import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.models import ChunkedEncodingError
import Settings as st

date_range = pd.date_range(st.startDate, st.currentDate)

#ghp_142WAP6ifjwTMD4VPNYr8LIkKtH94G7uh2sw7PL
def scrapRainfallData():
    for datevalue in date_range:
        formattedDate = datevalue.strftime('%Y-%m-%d')
        Url =  f'{st.SiteUrl}{formattedDate}'
        print(f"Retreiveing datat for {formattedDate}")
        webScrapping(Url)
        

def webScrapping(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
    data_iterator = iter(soup.find_all('td'))
    while True:
             try:
                 Location = next(data_iterator).text
                 ActualMM = next(data_iterator).text
                 NormalMM = next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 print(f'{Location} : {ActualMM} : {NormalMM}')
             except Exception as err:
                 break          
     

scrapRainfallData()
# Problem 4 - Inject the data in MongoDB
    
