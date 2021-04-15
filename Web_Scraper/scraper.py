from bs4 import BeautifulSoup as bs
import requests

# get source html file with http request
req = requests.get('https://www.mountainproject.com/gyms/florida').text

# takes request and parses with lxml
soup = bs(req,'lxml')

# Returns a list of scraped gyms within div climbing_gyms
for gym in soup.find_all(class_='text-truncate'):

    #print('%s ==> %s' %(gym.text, gym.a['href']))
    #print('⭐⭐⭐⭐⭐')

    # Open up output html file for display
    f = open("climbing_gyms.html", "a")
    # For each gym add Gym name and link to output html file
    f.write("<h1>{0}<h1> ==> <a href='{1}'>{1}</a><br><br>".format(gym.text, gym.a['href']))
    # Rating 
    f.write("⭐⭐⭐⭐⭐")
    # Close file 
    f.close()