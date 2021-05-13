import pandas as pd
import requests
import numpy as np
import re
import json

#import secrets from key.py
from keys import GKEY

#safely splits up column with list

def getFirstItem(gym_info: list):
    try:
        return gym_info[0]
    except:
        return ""

def getSecondItem(gym_info: list):
    try:
        return gym_info[1]
    except:
        return ""

#grab non-nested values with try-except
def tryToGet(searchResults, resultKey: str, isList: bool = False):
    try:
        return searchResults[resultKey]
    except:
        if not isList:
            return ""
        else:
            return []

def loadGymDf(filepath: str = 'data.json'):
    #load the scrapped data from mountainProject(mP)
    df = pd.read_json(filepath, orient='index')

    # split up list column
    df['gymURL'] = df['gym_info'].map(getFirstItem)
    df['gym_address'] = df['gym_info'].map(getSecondItem)
    del df['gym_info']

    #create empty columns to fill
    df["google_Place_ID"] = ""
    df["locLat"] = ""
    df["locLong"] = ""
    df["business_status"] = ""
    df["google_photoReferences"] = ""
    df["googleRating"] = ""
    df["numUsersRated"] = ""
    df["typeList"] = ""

    return df

if __name__ == "__main__":
    #load gym dataframe
    df = loadGymDf()

    #specify the url endpoint, and fields to request
    placeTextSearchURL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    fields = [
            "place_id",
            "business_status",
            "rating",
            "types",
            "user_ratings_total",
            "name",
            "geometry",
            'photos'
        ]
    #For testing perposes, script will be run on just Delaware's 4 gyms
    df = df[df['state'] == 'Delaware'] #this line must be removed when done testing


    for idx, row in df.iterrows():

        #assign address to variable, and create params dict
        address = row['locName'].strip('…') + " " + row['gym_address']
        
        params = {
                    "key": GKEY,
                    "query": address,
                    'fields':fields
                }
        #get request to location text search api endpoint
        searchResults = requests.get(placeTextSearchURL, params=params)
        
        #conv to dict for easy extract
        searchResults = searchResults.json()
        
        #if results are empty, attmept a second search with just name
        if not searchResults["results"]:
            params.update({'query': row['locName'].strip('…')})
            searchResults = requests.get(placeTextSearchURL, params=params).json()
        
        if searchResults["results"]:
            searchResults = searchResults["results"][0]

        # extract non-nested value
        df.loc[idx,"google_Place_ID"] = tryToGet(searchResults,  "place_id")
        df.loc[idx,"business_status"] = tryToGet(searchResults,  "business_status")
        df.loc[idx,"googleRating"] = tryToGet(searchResults,"rating")
        df.at[idx,"typeList"] = tryToGet(searchResults, "types", True)
        df.loc[idx,"numUsersRated"] = tryToGet(searchResults, "user_ratings_total")
        
        #Try and update cleaner name
        try:
            df.loc[idx,"locName"] = searchResults["name"]
        except:
            pass
        
        #manual try blocks for nested values
        try:
            df.loc[idx,"locLat"] = searchResults["geometry"]["location"]["lat"]
            df.loc[idx,"locLong"] = searchResults["geometry"]["location"]["lat"]
        except:
            df.loc[idx,"locLat"] = np.nan
            df.loc[idx,"locLong"] = np.nan
            
        #naual try blocks for photolist
        try:
            photoReferenceList = []
            for photo in searchResults['photos']:
                photoReferenceList.append(photo["photo_reference"])
            df.at[idx,"google_photoReferences"] = photoReferenceList
        except:
            df.at[idx,"google_photoReferences"] = []
    
