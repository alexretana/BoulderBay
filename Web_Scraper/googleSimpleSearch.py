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
    # sends GET req with user search var attached in google api URL
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=textquery&fields=photos,place_id,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyAhv0uH1F1KkSjDVJwFzGBagH9tEFSDbcs"%(searchloc)
    res = (requests.get(url).text)
    
    try:
        # access res loaded as JSON dictionary
        lat = json.loads(res)['candidates'][0]['geometry']['location']['lat']
        lng = json.loads(res)['candidates'][0]['geometry']['location']['lng']
        rating = json.loads(res)['candidates'][0]["rating"]
        place_id = str(json.loads(res)['candidates'][0]["place_id"])
        photos = str(json.loads(res)['candidates'][0]["photos"][0]['photo_reference'])
        name = str(json.loads(res)['candidates'][0]["name"])
    
        # return geo location and rating for Google infomation
        return {
            "correct_name":name,
            "geoLoc":[lat,lng],
            "place_id":place_id,
            "rating":rating,
            "gphotos_ref":photos
            
        }

    except:
        # If error occurs return NA for both geo and rating values and continue
        print ('\n...===> Weird stuff happened with this one \n(%s)\n ..moving on <===\n'%(searchloc))
        return {
            "correct_name":"NA",
            "geoLoc":"NA",
            "rating":"NA",
            "place_id":"NA",
            "rating":"NA",
            "gphotos_ref":"NA"
        }
        pass
   
    

# print (getGInfo('projectROCK'))