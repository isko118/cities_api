from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class CityDB(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class City(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class CityCreate(BaseModel):
    name: str
