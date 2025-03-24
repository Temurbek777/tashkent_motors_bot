from db_handler.create_db import SessionLocal, Car, CarPhoto
from collections import defaultdict
from sqlalchemy import select, distinct, func


light_cars = select(Car.brand, Car.model).where(Car.car_type == "Yengil")

def get_all_light_car_brands():
    "Retrive all car brands"
    db = SessionLocal()
    try:
        result = db.execute(light_cars).fetchall()
    finally:
        db.close()

    # Group models by brand using a defaultdict
    light_car_brand_models = defaultdict(set)  # using set to avoid duplicate models per brand
    for brand, model in result:
        light_car_brand_models[brand].add(model)

    # Optionally, convert sets to lists:
    brands_models = {brand: list(models) for brand, models in light_car_brand_models.items()}

    return brands_models


# print(get_all_light_car_brands())


trucks = select(Car.brand, Car.model).where(Car.car_type == "Yuk")

def get_all_truck_brands():
    "Retrive all truck brands"
    db = SessionLocal()
    try:
        result = db.execute(trucks).fetchall()
    finally:
        db.close()

    # Group models by brand using a defaultdict
    truck_brand_models = defaultdict(set)  # using set to avoid duplicate models per brand
    for brand, model in result:
        truck_brand_models[brand].add(model)

    # Optionally, convert sets to lists:
    brands_models = {brand: list(models) for brand, models in truck_brand_models.items()}

    return brands_models

# print(get_all_truck_brands())