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
    car_filtered = {k: v for k, v in car_data.items() if v not in (None, '0')}

    return car_filtered

print(get_car_by_model_filtered("J7"))