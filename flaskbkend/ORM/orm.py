from sqlalchemy import create_engine, text, Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, VARCHAR, DECIMAL, BOOLEAN, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship, scoped_session, sessionmaker
#running this file emitts DDL, but must remove the part in brakets: [ORM.]keys
from ORM.keys import DB_USER, DB_PASSWORD, DB_ENDPOINT

#import connection info
user = DB_USER
pwd = DB_PASSWORD
endpoint = DB_ENDPOINT

#create url for engin
dialect = f"mysql+pymysql://{user}:{pwd}@{endpoint}/boulderinggyms"

#create engind and bind to session
Base = declarative_base()
metadata = Base.metadata

#Create a sessionmaker for other files to call
Session = scoped_session(sessionmaker())

#define table connected to clases
gyms_table = Table(
    "gyms",
    metadata,
    Column('gymID', BIGINT(unsigned=True), primary_key=True, autoincrement=True),
    Column('gymName', VARCHAR(80), nullable=False),
    Column('gymNameFromGoogle', VARCHAR(80)),
    Column('gymAddress', VARCHAR(100)),
    Column('gymState', VARCHAR(14)),
    Column('isOperational', VARCHAR(18)),
    Column('locLatitude', DECIMAL(8,6)),
    Column('locLongitude', DECIMAL(8,6)),
    Column('ratingFromGoogle', DECIMAL(2,1)),
    Column('numGoogleUsersRated', INTEGER(unsigned=True)),
    Column('googlePlaceID', VARCHAR(255)),
    Column('typeListStr', VARCHAR(255)),
    Column('lastUpdated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    UniqueConstraint('gymName')
)

photos_table = Table(
    "photos",
    metadata,
    Column('photoID', BIGINT(unsigned=True), primary_key=True, autoincrement=True),
    Column('gymID', BIGINT(unsigned=True), ForeignKey('gyms.gymID'), nullable=False),
    Column('photoGoogleReference', VARCHAR(255)),
    Column('photoURL', VARCHAR(1200)),
    Column('lastUpdated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
)

reviews_table = Table(
    "reviews",
    metadata,
    Column('reviewID', BIGINT(unsigned=True), primary_key=True, autoincrement=True),
    Column('gymID', BIGINT(unsigned=True), ForeignKey('gyms.gymID'), nullable=False),
    Column('author', VARCHAR(128)),
    Column('content', VARCHAR(5000), nullable=False),
    Column('rating', DECIMAL(2,1)),
    Column('timePosted', TIMESTAMP),
    Column('source', VARCHAR(24), nullable=False),
    Column('lastUpdated', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
)

#load configs for other files
def loadConfigs():
    return{
        'url' : dialect,
        'future' : True
    }

class Gym(Base):
    __table__ = gyms_table
    
    photo = relationship("Photo", back_populates="gym")
    review = relationship("Review", back_populates="gym")
    
    def __repr__(self):
        return f"Gym(gymID = {self.gymID!r}, \
            gymName = {self.gymName!r}, \
            gymNameFromGoogle = {self.gymNameFromGoogle!r}, \
            gymAddress = {self.gymAddress!r},  \
            gymState = {self.gymState!r}, \
            isOperational = {self.isOperational!r}, \
            locLatitude = {self.locLatitude!r}, \
            locLongitude = {self.locLongitude}, \
            ratingFromGoogle = {self.ratingFromGoogle!r}, \
            googlePlaceID = {self.googlePlaceID!r}, \
            typeListStr = {self.typeListStr!r}, \
            lastUpdated = {self.lastUpdated!r})"
    
class Photo(Base):
    __table__ = photos_table
    
    gym = relationship("Gym", back_populates="photo")
    
    def __repr__(self):
        return f"Photo(photoID = {self.photoID!r}, \
            gymID = {self.gymID!r}, \
            photoGoogleReference = {self.photoGoogleReference!r}, \
            photoURL = {self.photoURL!r}, \
            lastUpdated = {self.lastUpdated!r})"

class Review(Base):
    __table__ = reviews_table

    gym = relationship("Gym", back_populates="review")
    def __repr__(self):
        contentLen = len(self.content)
        return f"Review(reviewID = {self.reviewID!r}, \
            gymID = {self.gymID!r}, \
            author = {self.author!r}, \
            rating = {self.rating!r}, \
            time posted = {self.timePosted!r}, \
            source = {self.source!r}, \
            content has {contentLen} characters)"


#if orm is run, it builds tables for db
if __name__== '__main__':
    engine = create_engine(dialect, echo=True, future=True)
    metadata.create_all(engine)

