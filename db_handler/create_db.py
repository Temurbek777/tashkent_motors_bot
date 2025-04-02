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
    year = Column(String, nullable=False)
    position = Column(String, nullable=True)
    battery_capacity = Column(String, nullable=True)
    price = Column(String, nullable=True)
    condition = Column(String, nullable=True)
    body_type = Column(String, nullable=True)
    engine_type = Column(String, nullable=True)
    engine_size = Column(String, nullable=True)
    horsepower = Column(String, nullable=True)
    car_type = Column(String, nullable=True)
    transmission = Column(String, nullable=True)
    privod = Column(String, nullable=True)
    fuel_spending = Column(String, nullable=True)
    length = Column(String, nullable=True)
    height = Column(String, nullable=True)
    width = Column(String, nullable=True)
    disk_diameter = Column(String, nullable=True)
    clearance = Column(String, nullable=True)
    cargo_capacity = Column(String, nullable=True)
    seat_capacity = Column(String, nullable=True)
    lift_capacity = Column(String, nullable=True)
    battery_type = Column(String, nullable=True)
    mileage = Column(String, nullable=True)
    guarantee = Column(String, nullable=True)
    color = Column(String, nullable=True)
    bistr_zaryad = Column(String, nullable=True)
    home_zaryad = Column(String, nullable=True)
    is_ac_available = Column(Boolean, default=False)
    is_cruise_control_available = Column(Boolean, default=False)
    is_luk_available = Column(Boolean, default=False)
    is_display_available = Column(Boolean, default=False)
    is_seat_heat_available = Column(Boolean, default=False)
    is_360_kamera_available = Column(Boolean, default=False)
    is_auto_parking_available = Column(Boolean, default=False)

    # Relationship to the CarPhoto model
    photos = relationship("CarPhoto", back_populates="car", cascade="all, delete-orphan")

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    view_count = Column(Integer, default=0)
    request_count = Column(Integer, default=0)
    action_date = Column(String, nullable=True)

# Create the database tables
Base.metadata.create_all(bind=engine)



# Call the function to create a new car with multiple photos
