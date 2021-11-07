import requests
from bs4 import BeautifulSoup
from requests.models import ChunkedEncodingError

startDate = '2021-01-01'
currentDate = '2021-11-07'
rainfallDate = '2021-11-07'


# Problem 1 - Write a function to loop between startDate and currentDate and pass the value to below url
URL =  f'http://122.15.179.102/ARS/home/rainfall/{rainfallDate}'
r = requests.get(URL)
  

# Problem 2 - Create function to handle the webscrapping
# Problem 3 - Call the function in Problem 1 function
soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
data = []
 
td_iterator = iter(soup.find_all('tr'))
data_iterator = iter(td_iterator.find_all('td'))
while True:
    try:
        Location = next(data_iterator).text
        ActualMM = next(data_iterator).text
        NormalMM = next(data_iterator).text 
        # For 'confirmed' and 'deaths',
        # make sure to remove the commas
        # and convert to int
        print(f'{Location} : {ActualMM} : {NormalMM}')
    except StopIteration:
        break
    
