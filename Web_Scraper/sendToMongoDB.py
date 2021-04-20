import json
from pymongo import MongoClient


# loads in data.json 
json_file = open('data.json')

# returns JSON object as a dictionary 
data = json.load(json_file)

for x in data:
    print (data[x])