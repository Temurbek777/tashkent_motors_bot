from db_handler.create_db import SessionLocal, Car, CarPhoto
from collections import defaultdict
from sqlalchemy import select, distinct, func


stmt = select(Car.brand, Car.model)

def get_all_car_brands():
    "Retrive all car brands"
    db = SessionLocal()
    try:
        result = db.execute(stmt).fetchall()
    finally:
        db.close()

    # Group models by brand using a defaultdict
    brands_models = defaultdict(set)  # using set to avoid duplicate models per brand
    for brand, model in result:
        brands_models[brand].add(model)

    # Optionally, convert sets to lists:
    brands_models = {brand: list(models) for brand, models in brands_models.items()}

    print(brands_models)

get_all_car_brands()
