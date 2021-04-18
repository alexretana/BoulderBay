from bs4 import BeautifulSoup as bs
import requests
import json

# get source html file with http request
req = requests.get('https://www.mountainproject.com/gyms/florida').text

# takes request and parses with lxml
soup = bs(req,'lxml')
gym_data = {}
# Returns a list of scraped gyms within div climbing_gyms
for gym in soup.find_all(class_='text-truncate'):


    """ scrape each link and follow each link in gym index homepage
        then store results in a dictionary with name of gym as key and link
        and images as values
    """
    # get request to link"
    link = gym.find('a')['href']
    page_r = requests.get(link).text
    
    # takes request and parse with lXML
    gym_list_name = gym.find('a').text
    #print (gym_list_name)
    gym_list = []
    gym_page = bs(page_r,'lxml')

    # for each gym page search for img tag
    for img in gym_page.find_all(class_ ='lazy'):
        # getting img data src
        if 'smallMed' in (img)['data-original']:
            #storing img links in gym_list
            gym_list.append((img)['data-original'])
            #print  ((img)['data-original'])

    # takes imgs and add to gym_data
    new_gym_list = [x for x in gym_list]
    gym_data[gym_list_name] = new_gym_list

# from python object to json then write file
print (gym_data)
with open('data.json', 'w') as outfile:
    json.dump(gym_data, outfile,indent=4)

            
    
    

        # for each link follow and scrape photo and count rating star images





    