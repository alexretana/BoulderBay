from bs4 import BeautifulSoup as bs4
import requests, json

# term = 'Gadrock'
# Func takes location name and google search for rating

# def getRating(searchloc):
#     # replace spaces with +
#     location = searchloc.replace(' ','+')
#     #location = 'First+Avenue+Rocks'
#     # req to google with location attached
#     res = requests.get('https://google.com/search?q='+ location)
#     # soupin it ...
#     soup = bs4(res.text,'lxml')
#     # grabs reoccuring rating pattern
#     result = (soup.select('span')[16].text[0:4])
#     return result
#     # if decimal point in result return value (gives error)
#     # if '.' in result:
#     #     return float(result.replace(' ',''))
#     # else: 
#     #     return 0

# # print (getRating('First+Avenue+Rocks'))

def getGInfo(searchloc):

    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAhv0uH1F1KkSjDVJwFzGBagH9tEFSDbcs"%(searchloc)
    res = (requests.get(url).text)
    lat = json.loads(res)['candidates'][0]['geometry']['location']['lat']
    lng = json.loads(res)['candidates'][0]['geometry']['location']['lng']
    rating = json.loads(res)['candidates'][0]["rating"]
   
    return {
        "geoLoc":[lat,lng],
        "rating":rating
    }
    

print (getGInfo('projectROCK'))