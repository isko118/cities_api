from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import City, CityCreate
from app.services import add_city, delete_city, get_cities, find_nearest_cities


router = APIRouter()


@router.post('/cities', response_model=City)
def create_city(city_create: CityCreate, db: Session = Depends(get_db)):
    city = add_city(db, city_create)
    if city is None:
        raise HTTPException(
            status_code=400,
            detail="City already exists or could not find coordinates."
        )
    return city


@router.delete('/cities/{city_id}', response_model=dict)
def remove_city(city_id: int, db: Session = Depends(get_db)):
    success = delete_city(db, city_id)
    if not success:
        raise HTTPException(status_code=404, detail="City not found.")
    return {'detail': 'City deleted'}


@router.get('/cities', response_model=List[City])
def list_cities(db: Session = Depends(get_db)):
    return get_cities(db)


@router.get('/nearest_cities', response_model=List[City])
def nearest_cities(lat: float, lon: float, db: Session = Depends(get_db)):
    cities = find_nearest_cities(db, lat, lon)
    if not cities:
        raise HTTPException(status_code=404, detail="No cities found.")
    return cities
