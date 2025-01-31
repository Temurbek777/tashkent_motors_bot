from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Float,Boolean
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
import shutil
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of create_db.py
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'Tashkent Motors DB.db')}"  # Absolute path
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CarPhoto(Base):
    __tablename__ = 'car_photo'

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)  # Foreign key to the Car table
    photo_url = Column(String, nullable=False)  # URL or file path of the photo

    # Relationship to the Car model
    car = relationship("Car", back_populates="photos")

# Define the Car model
class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    position = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    condition = Column(String, nullable=True)
    body_type = Column(String, nullable=True)
    engine_type = Column(String, nullable=True)
    engine_size = Column(Float, nullable=True)
    horsepower = Column(Integer, nullable=True)
    torque = Column(Integer, nullable=True)
    transmission = Column(String, nullable=True)
    privod = Column(String, nullable=True)
    fuel_spending = Column(Float, nullable=True)
    length = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    width = Column(Float, nullable=True)
    disk_diameter = Column(Float, nullable=True)
    clearance = Column(Float, nullable=True)
    cargo_capacity = Column(Float, nullable=True)
    seat_capacity = Column(Integer, nullable=True)
    lift_capacity = Column(Float, nullable=True)
    battery_type = Column(String, nullable=True)
    mileage = Column(Float, nullable=True)
    guarantee = Column(String, nullable=True)
    color = Column(String, nullable=True)
    is_ac_available = Column(Boolean, default=False)
    is_cruise_control_available = Column(Boolean, default=False)
    is_luk_available = Column(Boolean, default=False)
    is_display_available = Column(Boolean, default=False)
    is_seat_heat_available = Column(Boolean, default=False)
    is_360_kamera_available = Column(Boolean, default=False)
    is_auto_parking_available = Column(Boolean, default=False)

    # Relationship to the CarPhoto model
    photos = relationship("CarPhoto", back_populates="car")

# Create the database tables
Base.metadata.create_all(bind=engine)

def create_car_with_photos():
    db = SessionLocal()

    # Create a new car
    new_car = Car(
        brand="Toyota",
        model="Camry",
        year=2022,
        position="Sedan",
        price=30000.0,
        condition="New",
        body_type="Sedan",
        engine_type="Gasoline",
        engine_size=2.5,
        horsepower=203,
        torque=184,
        transmission="Automatic",
        fuel_spending=7.1,
        length=4885,
        height=1445,
        width=1840,
        disk_diameter=18,
        clearance=160,
        cargo_capacity=524,
        seat_capacity=5,
        lift_capacity=0,
        battery_type=None,
        mileage=0,
        guarantee="3 years",
        color="White",
        is_ac_available=True,
        is_cruise_control_available=True,
        is_display_available=True,
        is_seat_heat_available=False,
        is_360_kamera_available=False,
        is_auto_parking_available=False
    )

    # Add the car to the session
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    # Add multiple photos for the car
    photo1 = CarPhoto(photo_url="path/to/photo1.jpg", car_id=new_car.id)
    photo2 = CarPhoto(photo_url="path/to/photo2.jpg", car_id=new_car.id)
    photo3 = CarPhoto(photo_url="path/to/photo3.jpg", car_id=new_car.id)

    db.add_all([photo1, photo2, photo3])
    db.commit()

    db.close()

# Call the function to create a new car with multiple photos
