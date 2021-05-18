from flask import Flask, json, request
from sqlalchemy import create_engine
from decimal import Decimal
from datetime import datetime

from ORM.orm import Gym, Photo, Session, loadConfigs

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

    args = request.args
    if set(['locLatitude', 'locLongitude']).issubset(set(args)):
        try:
            locLat = float(args.get('locLatitude'))
            locLong = float(args.get('locLongitude'))\

            return app.response_class(
                response=json.dumps({
                        'latCoord': locLat,
                        'longCoord' : locLong
                    }, 
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