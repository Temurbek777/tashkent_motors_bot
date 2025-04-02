from db_handler.create_db import SessionLocal, Car, CarPhoto

def Get_Car_models():
    stats={}
    db = SessionLocal()
    cars = db.query(Car).all()
    for car in cars:
        stats[f"{car.model}"]=0
    return stats

# print(Get_Car_models())