from flask import Flask, json, request
from sqlalchemy import create_engine, and_
from decimal import Decimal
from datetime import datetime
import numpy as np

from ORM.orm import Gym, Photo, Session, loadConfigs

#set Earth's radius as const (in miles)
EARTH_RADIUS = 3958.8
FIFTY_MILES = 50.0

app = Flask(__name__)

#load configs and initialize sqlalchemy session
config = loadConfigs()
engine = create_engine(**config)
Session.configure(bind=engine)
session = Session()

#deals with sqlalch returns that cant be jsonified
def makeJsonSerializable(jsonValue):
    if isinstance(jsonValue, datetime):
        return jsonValue.isoformat()
    elif isinstance(jsonValue, Decimal):
        return float(jsonValue)

# returns index with gymName as pyth dict
def indexTupleToDict(tup):
    return {
        'gymID' : tup[0],
        'gymName' : tup[1]
    }

def queryFiftyMiles(locLat, locLong):
    locHeight = FIFTY_MILES / EARTH_RADIUS * 180.0 / np.pi #conv rad -> deg
    locLatRange = [locLat - locHeight, locLat + locHeight]

    locWidth = FIFTY_MILES / (EARTH_RADIUS * np.cos(locLat * np.pi / 180.0)) * 180.0 / np.pi #conv cos(deg-> rad) rad -> deg
    locLongRange = [locLong - locWidth, locLong + locWidth]

    whereStmt1 = and_(
        Gym.locLatitude > locLatRange[0],
        Gym.locLatitude < locLatRange[1]
    )
    whereStmt2 = and_(
        Gym.locLongitude > locLongRange[0], 
        Gym.locLongitude < locLongRange[1]
    )
    gymsWithinRange = session.query(Gym).filter(whereStmt1).filter(whereStmt2).all()
    return gymsWithinRange


#route to retrieve all gyms
@app.route('/gyms/')
def getAllGyms():
    
    
    #sqlalchemy query to db
    gyms = session.query(Gym.gymID, Gym.gymName).all()
    
    # creates response
    gymsResponse = []
    for gym in gyms:
        gymsResponse.append(indexTupleToDict(gym))
    
    response = app.response_class(
        response=json.dumps(gymsResponse, default=makeJsonSerializable),
        status=200,
        mimetype='application/json'
    )
    
    return response

@app.route('/searchForGyms')
def searchForGyms():

    #checks for parameters and if they can be conv -> float
    args = request.args
    if set(['lat', 'lng']).issubset(set(args)):
        try:
            locLat = float(args.get('lat'))
            locLong = float(args.get('lng'))

            #attempts to query gyms within range
            try:
                gyms = queryFiftyMiles(locLat, locLong)
            except:
                return "Failed query", 404

            #creates response    
            gymsResponse = []
            for gym in gyms:
                gym.__dict__.pop("_sa_instance_state")
                gymsResponse.append(gym.__dict__)

            return app.response_class(
                response=json.dumps(gymsResponse, 
                default=makeJsonSerializable),
                status=200,
                mimetype='application/json'
            )
        except:
            return "Failed to convert coordinates to floats", 404
    else:
        return "Latitude and Longitude parameters not provided", 404
   
#route to retrieve a specific gyms
@app.route('/gyms/<int:gymID>')
def getGymInfo(gymID : int):

    return 

if __name__ == "__main__":
    app.run(debug=True)