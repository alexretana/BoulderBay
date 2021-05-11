from bs4 import BeautifulSoup as bs
import requests
import json
from time import sleep
import logging 
from googleSimpleSearch import getGInfo
from config import listOfStates

logging.basicConfig(filename="errors.log", level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

# scrapes info and images from RC Gyms per State
def scrapeStateFromMoutainProject(state):
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
        gym_list_name = gym.find('a').text.encode('utf-8')
        
        # print(("getting info on %s") %(gym_list_name))
        if '\xe2' in gym_list_name:
            try:
                logging.warning('\n*** Dots ... in %s***\n' %(gym_list_name))
                # Follow gym_list_name and get full name instead of ...X
                for  line in (bs(requests.get(link).text,'lxml').find_all(id='climbing-gyms')):
                    print (str(line.find('h1').text.strip().decode('utf-8')))
                    cleaned_title = str(line.find('h1').text.strip().decode('utf-8'))
                    gym_data[cleaned_title] = {}
                    # adding location name to gym data object
                    gym_data[cleaned_title]['locName'] = cleaned_title
                    # adding state to gym data object
                    gym_data[cleaned_title]["state"] = state
                    # use Google api to get geoLoc and rating 
                    gym_data[cleaned_title]['googleInfo'] = getGInfo(cleaned_title)
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
                    gym_data[cleaned_title]['img_list'] = gym_list
                    # for each gym page search for gym-info class
                    for gym_info in gym_page.find_all(class_="gym-info"):

                        gym_data[cleaned_title]['gym_info'] = [
                        a.text for a in gym_info.find_all('a')]
            except:

                    logging.warning('Some major shit went wrong ... moving on')
                    pass
        else:
            try:
                print(gym_list_name)
                gym_data[gym_list_name] = {}

                # adding location name to gym data object
                gym_data[gym_list_name]['locName'] = gym_list_name
                # adding state to gym data object
                gym_data[gym_list_name]["state"] = state

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
                    a.text for a in gym_info.find_all('a')]
            except:

                logging.warning('Some major shit went wrong ... moving on')
                pass

        # wait 1 second before next state
        print("\n Waiting 1 seconds per request... zzz\n")
        sleep(1)

    return gym_data

if __name__ == "__main__":
    
    # initiallizes dict to dump data into
    gym_data = {}
    # success count
    count = 0
    # test list override
    
    # loop through each state to scrap
    for state in listOfStates:
        print ("\n *** Getting goodies from ... %s ***\n"%(state))
        state = state.replace(" ", "-")
        
        try:
            scrapped_gym_data = scrapeStateFromMoutainProject(state)
            count+=1
        except:
            pass
``
        # print (scrapped_gym_data)
        # append to full dictionary list
        gym_data.update(scrapped_gym_data)

        # wait ten second before next state
        print("\n Waiting 10 seconds until next state... zzz\n")
        sleep(10)

        # # write to json for every state
        with open('data.json', 'w') as outfile:
            json.dump(gym_data, outfile,indent=4)
            print ("All data from %s state/s now successfully written to file!" %(count))
