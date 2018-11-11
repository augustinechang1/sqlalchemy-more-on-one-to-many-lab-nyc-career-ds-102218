from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below
class Players(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    number = Column(Integer)
    height = Column(String)
    weight = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Teams', back_populates = 'player')

class Teams(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    city_id = Column(Integer, ForeignKey('city.id'))
    sport_id = Column(Integer, ForeignKey('sports.id'))
    player = relationship('Players', back_populates = 'team')
    sport = relationship('Sports', back_populates = 'team')
    city = relationship('City', back_populates = 'team')

class Sports(Base):
    __tablename__ = "sports"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    team = relationship('Teams', back_populates = 'sport')

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    state = Column(Text)
    team = relationship('Teams', back_populates = 'city')

engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
