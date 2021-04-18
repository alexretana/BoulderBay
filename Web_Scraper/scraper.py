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
    gym_data[gym_list_name] = {}
    print ("\n Getting info on ... " + gym_list_name + "\n")
    gym_list = []
    gym_page = bs(page_r,'lxml')

    # for each gym page search for img tag
    for img in gym_page.find_all(class_ ='lazy'):
        # getting img data src based on class smallMed
        if 'smallMed' in img['data-original']:
            #storing img links in gym_list
            gym_list.append((img)['data-original'])
            #print  ((img)['data-original'])

    # takes imgs and add to gym_data
    new_gym_list = [x for x in gym_list]
    gym_data[gym_list_name]['img_list'] = new_gym_list

    # for each gym page search for gym-info class
    for gym_info in gym_page.find_all(class_= "gym-info"):

        gym_data[gym_list_name]['gym_info'] = [str(a.text) for a in gym_info.find_all('a')]
        
        
        







# from python object to json then write file

with open('data.json', 'w') as outfile:
    json.dump(gym_data, outfile,indent=4)

            
    
    

        # for each link follow and scrape photo and count rating star images





    