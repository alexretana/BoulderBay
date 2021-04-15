from bs4 import BeautifulSoup as bs
import requests

# Opens gyms.html code to parse
with open('gyms.html') as gyms_file:
    soup = bs(gyms_file,'lxml')

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