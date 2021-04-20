import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://dboi:<password>@cluster0.pon7o.mongodb.net/climbingDB?retryWrites=true&w=majority")
db = client.test

if db:print('workin')
# # loads in data.json 
# json_file = open('data.json')

# # returns JSON object as a dictionary 
# data = json.load(json_file)

# for x in data:
#     print (data[x])