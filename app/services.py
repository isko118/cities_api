from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List, Optional

from app.models import City, CityCreate, CityDB
from app.utils import get_coordinates
import math


def add_city(db: Session, city_create: CityCreate) -> Optional[City]:
    city_name = city_create.name
    latitude, longitude = get_coordinates(city_name)
    if latitude is None or longitude is None:
        return None

    db_city = CityDB(name=city_name, latitude=latitude, longitude=longitude)
    try:
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
    except IntegrityError:
        db.rollback()
        return None
    return City.from_orm(db_city)


def delete_city(db: Session, city_id: int) -> bool:
    db_city = db.query(CityDB).filter(CityDB.id == city_id).first()
    if db_city is None:
        return False
    db.delete(db_city)
    db.commit()
    return True


def get_cities(db: Session) -> List[City]:
    db_cities = db.query(CityDB).all()
    return [City.from_orm(city) for city in db_cities]


def find_nearest_cities(db: Session, latitude: float, longitude: float) -> List[City]:
    cities = get_cities(db)
    cities.sort(key=lambda city: haversine(latitude, longitude, city.latitude, city.longitude))
    return cities[:2]


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) *
         math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance
