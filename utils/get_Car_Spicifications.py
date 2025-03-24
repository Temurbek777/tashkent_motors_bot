from db_handler.create_db import SessionLocal, Car, CarPhoto

def get_car_by_model_filtered(model_name: str):
    """
    Retrieve car details by model but exclude attributes that are 0 or NULL.
    """
    db = SessionLocal()
    car = db.query(Car).filter(Car.model == model_name).first()

    if not car:
        print(f"No car found for model: {model_name}")
        return None

    # Convert car object to dictionary and remove zero/None values
    car_data = {column.name: getattr(car, column.name) for column in Car.__table__.columns}
    car_filtered = {k: v for k, v in car_data.items() }

    return car_filtered


# if v not in (None, '0')

# specifications = get_car_by_model_filtered("J7")

# print(specifications)
# print(specifications['id'])

def get_car_photo_by_model_filtered(model_name: str):
    db = SessionLocal()
    car = db.query(Car).filter(Car.model == model_name).first()
    car_photo = db.query(CarPhoto).filter(CarPhoto.car_id == car.id).all()
    # for photo in car_photo:
    #     print(photo.photo_url)

    if not car:
        print(f"No car photo found for model: {model_name}")
        return None
    return car_photo

# get_car_photo_by_model_filtered("Yuan Plus")

