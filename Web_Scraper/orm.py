from sqlalchemy import create_engine, text, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DECIMAL, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship, Session
from key import DB_USER, DB_PASSWORD, DB_ENDPOINT

#import connection info
user = DB_USER
pwd = DB_PASSWORD
endpoint = DB_ENDPOINT

#create url for engin
dialect = f"mysql+pymysql://{user}:{pwd}@{endpoint}/boulderinggyms"

#create engind and bind to session
## Remove echo=True when done debugging
engine = create_engine(dialect, echo = True, future=True)
Base = declarative_base()
metadata = Base.metadata
session = Session

#if orm is run, it builds tables for db
if __name__== '__main__':
    metadata = Base.metadata