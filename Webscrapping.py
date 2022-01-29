from argparse import Action
from pandas.core.indexes.datetimes import date_range
import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.models import ChunkedEncodingError
import Settings as st
import matplotlib
import matplotlib.pyplot as plt

date_range = pd.date_range(st.startDate, st.currentDate)

#ghp_142WAP6ifjwTMD4VPNYr8LIkKtH94G7uh2sw7PL
def scrapRainfallData():
    for datevalue in date_range:
        formattedDate = datevalue.strftime('%Y-%m-%d')
        Url =  f'{st.SiteUrl}{formattedDate}'
        print(f"Retreiveing datat for {formattedDate}")
        webScrapping(Url,formattedDate)
        

def webScrapping(url,date):
    print("********************Rainfall Data*******************************")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
    data_iterator = iter(soup.find_all('td'))
    newdata = {}
    districtList = []
    actualRainfall = []
    normalRainfall = []
    while True:
             try:
                 Location = next(data_iterator).text
                 ActualMM = next(data_iterator).text
                 NormalMM = next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 next(data_iterator).text
                 districtList.append(Location) 
                 actualRainfall.append(float(str(ActualMM)))
                 normalRainfall.append(float(str(NormalMM)))
                 print(f'{Location} : {ActualMM} : {NormalMM}')
                 # Problem 3 - Push all data to pandas
                 # Problem 4 - Chart the data for each date
             except Exception as err:
                 break     
    
    print("********************End of Data*******************************") 
    newdata['Location'] = districtList
    newdata['ActualRainfall'] = actualRainfall
    newdata['NormalRainfall'] = normalRainfall
    df = pd.DataFrame(newdata,columns=['Location','ActualRainfall','NormalRainfall'])
    plt.plot(df.Location,df.NormalRainfall,linewidth=6,linestyle = '-')
    plt.plot(df.Location,df.ActualRainfall,'r--o',linewidth=4)
    plt.title(f'RainFall Data in mm for {date}')
    plt.legend(['Normal', 'Actual'])
    plt.xticks(rotation = 90.5)
    plt.show()
    df = pd.DataFrame() 
    print ("***********Added data to pandas***************")

scrapRainfallData()
# Problem 5 - Inject the data in MongoDB
    
