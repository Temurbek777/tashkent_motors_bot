from admin.insert_data import SessionLocal, Car, CarPhoto

db = SessionLocal()

cars = db.query(Car).all()
print("All Cars:")
for car in cars:
    print(f"ID: {car.id}, Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Price: {car.price}")

db.close()