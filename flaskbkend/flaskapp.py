from flask import Flask, json
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

def makeJsonSerializable(jsonValue):
    if isinstance(jsonValue, datetime):
        return jsonValue.isoformat()
    elif isinstance(jsonValue, Decimal):
        return float(jsonValue)



#route to retrieve all gyms
@app.route('/gyms/')
def getAllGyms():
    
    
    #sqlalchemy query to db
    gyms = session.query(Gym).all()
    
    # creates response
    gymsResponse = []
    for gym in gyms:
        #removes sqlalchmey state from response
        gym.__dict__.pop('_sa_instance_state')
        gymsResponse.append(gym.__dict__)

    response = app.response_class(
        response=json.dumps(gymsResponse, default= makeJsonSerializable),
        status=200,
        mimetype='application/json'
    )
    
    return response
    
   
#route to retrieve a specific gyms
@app.route('/gyms/<int:gymID>')
def getDboi():
    return 'dboi'