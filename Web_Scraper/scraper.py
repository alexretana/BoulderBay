from bs4 import BeautifulSoup as bs
import requests
import json
from time import sleep


# The list of states to scrap mountain project for
listOfStates = [
        'Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucy',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Caroline',
        'North Dakota',
        'Ohio',
        'Oklahoma',
        'Orgegon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming'
]
    
        

# func scrapes info and images from RC Gyms per State
def scrapeStateFromMoutainProject(state : int):
    # get source html file with http request
    state_url = 'https://www.mountainproject.com/gyms/' + state
    req = requests.get(state_url).text

    # takes request and parses with lxml
    soup = bs(req, 'lxml')
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
        print("\n Getting info on ... " + gym_list_name + "\n")
        gym_list = []
        gym_page = bs(page_r, 'lxml')

        # for each gym page search for img tag
        for img in gym_page.find_all(class_='lazy'):
            # getting img data src based on class smallMed
            if 'smallMed' in img['data-original']:
                #storing img links in gym_list
                gym_list.append(img['data-original'])
                #print  ((img)['data-original'])

        # takes imgs and add to gym_data
        gym_data[gym_list_name]['img_list'] = gym_list

        # for each gym page search for gym-info class
        for gym_info in gym_page.find_all(class_="gym-info"):

            gym_data[gym_list_name]['gym_info'] = [
                str(a.text) for a in gym_info.find_all('a')]

    return gym_data


if __name__ == "__main__":

    #initiallizes dict to dump data into
    gym_data = {}
    #test list override
    # listOfStates = ['Florida', 'New York']

    #loop through each state to scrap
    for state in listOfStates:
        state = state.replace(" ", "-")
        scrapped_gym_data = scrapeStateFromMoutainProject(state)

        #append to full dictionary list
        gym_data.update(scrapped_gym_data)

        #wait ten second before next state
        sleep(10)


# write to json
    with open('data.json', 'w') as outfile:
        json.dump(gym_data, outfile,indent=4)
