from bs4 import BeautifulSoup as bs
import requests

# get source html file with http request
req = requests.get('https://www.mountainproject.com/gyms/florida').text

# takes request and parses with lxml
soup = bs(req,'lxml')

# Returns a list of scraped gyms within div climbing_gyms
for gym in soup.find_all(class_='text-truncate'):

    # scrape each link and follow each link in gym index homepage
    
    # get request to link 
    link = gym.find('a')['href']
    gym_page = requests.get(link).text
    
    # for each gym page search for img tag
    

    
    


        # for each link follow and scrape photo and count rating star images





    