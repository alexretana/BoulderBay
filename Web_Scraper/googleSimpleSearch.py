from bs4 import BeautifulSoup as bs4
import requests

# term = 'Gadrock'
# Func takes location name and google search for rating

def getRating(searchloc):
    # replace spaces with +
    location = searchloc.replace(' ','+')
    #location = 'First+Avenue+Rocks'
    # req to google with location attached
    res = requests.get('https://google.com/search?q='+ location)
    # soupin it ...
    soup = bs4(res.text,'lxml')
    # grabs reoccuring rating pattern
    result = (soup.select('span')[16].text[0:4])
    return result
    # if decimal point in result return value (gives error)
    # if '.' in result:
    #     return float(result.replace(' ',''))
    # else: 
    #     return 0

# print (getRating('First+Avenue+Rocks'))