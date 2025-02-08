from tkinter import filedialog, messagebox
from PIL import Image
from pydantic.v1.networks import host_regex

from db_handler.create_db import Car, CarPhoto, SessionLocal
import os
import time
import customtkinter
import shutil

# Create the main window
app = customtkinter.CTk()
app.geometry("1500x900")
app.title("Add car")

custom_font = customtkinter.CTkFont(family="Arial", size=14, weight="bold")
data = {}
save_directory=""

#--------------------- car brand -------------------------------
# brand label
brand_lbl = customtkinter.CTkLabel(app, text="Brand", font=custom_font)
brand_lbl.place(x=100, y=80)

# brand text box
brand = customtkinter.CTkTextbox(app, width=200, height=30)
# brand.insert("0.0", "Brand of the car")
brand.place(x=90, y=110)
#---------------------------------------------------------------

#---------------------car model-------------------------------
# model label
model_lbl = customtkinter.CTkLabel(app, text="Model", font=custom_font)
model_lbl.place(x=400, y=80)

# model txt box
model = customtkinter.CTkTextbox(app, width=200, height=30)
model.place(x=390, y=110)
#----------------------------------------------------------------

#---------------------car year-------------------------------
# year label
year_lbl = customtkinter.CTkLabel(app, text="Year", font=custom_font)
year_lbl.place(x=700, y=80)

# year txt box
year = customtkinter.CTkTextbox(app, width=200, height=30)
year.place(x=690, y=110)
#----------------------------------------------------------------

#---------------------car position-------------------------------
# position label
position_lbl = customtkinter.CTkLabel(app, text="Position", font=custom_font)
position_lbl.place(x=1000, y=80)

# position txt box
position = customtkinter.CTkComboBox(app, values=['1chi pozitsiya', '2chi pozitsiya', '3chi pozitsiya', '4chi pozitsiya'], width=200, height=30)
position.place(x=990, y=110)
#----------------------------------------------------------------

#---------------------car Price-------------------------------
# Price label
price_lbl = customtkinter.CTkLabel(app, text="Price", font=custom_font)
price_lbl.place(x=100, y=200)

# Price txt box
price = customtkinter.CTkTextbox(app, width=200, height=30)

price.place(x=90, y=230)
#----------------------------------------------------------------

#---------------------car Condition-------------------------------
# Condition label
condition_lbl = customtkinter.CTkLabel(app, text="Condition", font=custom_font)
condition_lbl.place(x=400, y=200)

# Condition txt box
condition = customtkinter.CTkComboBox(app, values=['Yangi', 'Ishlatilgan'], width=200, height=30)
condition.place(x=390, y=230)
#----------------------------------------------------------------

#---------------------car Body type-------------------------------
# Body type label
body_type_lbl = customtkinter.CTkLabel(app, text="Body type", font=custom_font)
body_type_lbl.place(x=700, y=200)

# Body type txt box
body_type = customtkinter.CTkComboBox(app, values=['Sedan', 'Crossover', 'Pickup', 'Liftback'], width=200, height=30)
body_type.place(x=690, y=230)
#----------------------------------------------------------------

#---------------------car Engine type-------------------------------
# Engine type label
engine_type_lbl = customtkinter.CTkLabel(app, text="Engine type", font=custom_font)
engine_type_lbl.place(x=1000, y=200)

# Engine type box
engine_type = customtkinter.CTkComboBox(app, values=['Benzin', 'Dizel', 'Elektr', 'Gibrid'], width=200, height=30)
engine_type.place(x=990, y=230)
#----------------------------------------------------------------

#---------------------car Engine size-------------------------------
# Engine size label
engine_size_lbl = customtkinter.CTkLabel(app, text="Engine size", font=custom_font)
engine_size_lbl.place(x=100, y=320)

# Engine_size txt box
engine_size = customtkinter.CTkTextbox(app, width=200, height=30)
engine_size.place(x=90, y=350)
#----------------------------------------------------------------

#---------------------car HorsePower-------------------------------
# HorsePower label
horsePower_lbl = customtkinter.CTkLabel(app, text="HorsePower", font=custom_font)
horsePower_lbl.place(x=400, y=320)

# HorsePower txt box
horsePower = customtkinter.CTkTextbox(app, width=200, height=30)
horsePower.place(x=390, y=350)
#----------------------------------------------------------------

#---------------------car Torque-------------------------------
# Torque label
torque_lbl = customtkinter.CTkLabel(app, text="Torque", font=custom_font)
torque_lbl.place(x=700, y=320)

# Torque txt box
torque = customtkinter.CTkTextbox(app, width=200, height=30)
torque.place(x=690, y=350)
#----------------------------------------------------------------

#---------------------car Transmission-------------------------------
# Transmission label
transmission_lbl = customtkinter.CTkLabel(app, text="Transmission", font=custom_font)
transmission_lbl.place(x=1000, y=320)

# Transmission txt box
transmission = customtkinter.CTkComboBox(app, values=['Avtomat', 'Mexanik', 'Robot', 'Variator'], width=200, height=30)
transmission.place(x=990, y=350)
#----------------------------------------------------------------

#---------------------car Privod-------------------------------
# Privod label
privod_lbl = customtkinter.CTkLabel(app, text="Privod", font=custom_font)
privod_lbl.place(x=100, y=440)

# Privod txt box
privod = customtkinter.CTkComboBox(app, values=['Oldi', 'Orqa', '4 tomon'], width=200, height=30)
privod.place(x=90, y=470)
#----------------------------------------------------------------

#---------------------car Rasxod-------------------------------
# Rasxod label
rasxod_lbl = customtkinter.CTkLabel(app, text="Rasxod", font=custom_font)
rasxod_lbl.place(x=400, y=440)

# Rasxod txt box
rasxod = customtkinter.CTkTextbox(app, width=200, height=30)
rasxod.place(x=390, y=470)
#----------------------------------------------------------------

#---------------------car Uzunligi-------------------------------
# Uzunligi label
uzunligi_lbl = customtkinter.CTkLabel(app, text="Uzunligi", font=custom_font)
uzunligi_lbl.place(x=700, y=440)

# Uzunligi txt box
uzunligi = customtkinter.CTkTextbox(app, width=200, height=30)
uzunligi.place(x=690, y=470)
#----------------------------------------------------------------

#---------------------car Balandligi-------------------------------
# Balandligi label
balandligi_lbl = customtkinter.CTkLabel(app, text="Balandligi", font=custom_font)
balandligi_lbl.place(x=1000, y=440)

# Balandligi txt box
balandligi = customtkinter.CTkTextbox(app, width=200, height=30)
balandligi.place(x=990, y=470)
#----------------------------------------------------------------

#---------------------car Eni-------------------------------
# Eni label
eni_lbl = customtkinter.CTkLabel(app, text="Eni", font=custom_font)
eni_lbl.place(x=100, y=560)

# Eni txt box
eni = customtkinter.CTkTextbox(app, width=200, height=30)
eni.place(x=90, y=590)
#----------------------------------------------------------------

#---------------------car Diska diametri-------------------------------
# Diska diametri label
disk_diametr_lbl = customtkinter.CTkLabel(app, text="Diska diametri", font=custom_font)
disk_diametr_lbl.place(x=400, y=560)

# Diska diametri txt box
disk_diametr = customtkinter.CTkTextbox(app, width=200, height=30)
disk_diametr.place(x=390, y=590)
#----------------------------------------------------------------

#---------------------car Clearance-------------------------------
# Clearance label
clearance_lbl = customtkinter.CTkLabel(app, text="Clearance", font=custom_font)
clearance_lbl.place(x=700, y=560)

# Clearance txt box
clearance = customtkinter.CTkTextbox(app, width=200, height=30)
clearance.place(x=690, y=590)
#----------------------------------------------------------------

#---------------------car Cargo Capacity-------------------------------
# Cargo Capacity label
cargo_capacity_lbl = customtkinter.CTkLabel(app, text="Cargo Capacity", font=custom_font)
cargo_capacity_lbl.place(x=1000, y=560)

# Cargo Capacity txt box
cargo_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
cargo_capacity.place(x=990, y=590)
#----------------------------------------------------------------

#---------------------car Seat Capacity-------------------------------
# Seat Capacity label
seat_capacity_lbl = customtkinter.CTkLabel(app, text="Seat Capacity", font=custom_font)
seat_capacity_lbl.place(x=100, y=680)

# Seat Capacity txt box
seat_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
seat_capacity.place(x=90, y=710)
#----------------------------------------------------------------

#---------------------car Lifting Capacity-------------------------------
# Lifting Capacity label
lift_capacity_lbl = customtkinter.CTkLabel(app, text="Lifting Capacity", font=custom_font)
lift_capacity_lbl.place(x=400, y=680)

# Lifting Capacity txt box
lift_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
lift_capacity.place(x=390, y=710)
#----------------------------------------------------------------

#---------------------car Battery type-------------------------------
# Battery type label
battery_type_lbl = customtkinter.CTkLabel(app, text="Battery type", font=custom_font)
battery_type_lbl.place(x=700, y=680)

# Battery type txt box
battery_type = customtkinter.CTkTextbox(app, width=200, height=30)
battery_type.place(x=690, y=710)
#----------------------------------------------------------------

#---------------------car Probeg-------------------------------
# Probeg label
probeg_lbl = customtkinter.CTkLabel(app, text="Probeg", font=custom_font)
probeg_lbl.place(x=1000, y=680)

# Probeg txt box
probeg = customtkinter.CTkTextbox(app, width=200, height=30)
probeg.place(x=990, y=710)
#----------------------------------------------------------------

#---------------------car Garantiya-------------------------------
# Garantiya label
garantiya_lbl = customtkinter.CTkLabel(app, text="Garantiya", font=custom_font)
garantiya_lbl.place(x=100, y=800)

# Garantiya txt box
garantiya = customtkinter.CTkTextbox(app, width=200, height=30)
garantiya.place(x=90, y=830)
#----------------------------------------------------------------

#---------------------car Color-------------------------------
# Color label
color_lbl = customtkinter.CTkLabel(app, text="Color", font=custom_font)
color_lbl.place(x=400, y=800)

# Color txt box
color = customtkinter.CTkTextbox(app, width=200, height=30)
color.place(x=390, y=830)
#----------------------------------------------------------------

#---------------------car Bistri Zaryad-------------------------------
# Bistri Zaryad label
bistr_zaryad_lbl = customtkinter.CTkLabel(app, text="Bistri Zaryad", font=custom_font)
bistr_zaryad_lbl.place(x=700, y=800)

# Bistri Zaryad txt box
bistr_zaryad = customtkinter.CTkTextbox(app, width=200, height=30)
bistr_zaryad.place(x=690, y=830)
#----------------------------------------------------------------

#---------------------car Home Zaryad-------------------------------
# Home Zaryad label
home_zaryad_lbl = customtkinter.CTkLabel(app, text="Home Zaryad", font=custom_font)
home_zaryad_lbl.place(x=1000, y=800)

# Home Zaryad txt box
home_zaryad = customtkinter.CTkTextbox(app, width=200, height=30)
home_zaryad.place(x=990, y=830)
#----------------------------------------------------------------

#---------------------car Battery Capacity-------------------------------
# Battery Capacity label
battery_capacity_lbl = customtkinter.CTkLabel(app, text="Battery Capacity", font=custom_font)
battery_capacity_lbl.place(x=1260, y=80)

# Battery Capacity txt box
battery_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
battery_capacity.place(x=1250, y=110)
#----------------------------------------------------------------

#---------------------car Features-------------------------------
kond = customtkinter.CTkCheckBox(app, text='Konditsioner', width=200, height=30)
kond.place(x=1310, y=190)

cruise_control = customtkinter.CTkCheckBox(app, text="Adaptive kruiz kontrol", width=200, height=30)
cruise_control.place(x=1310, y=240)

luk = customtkinter.CTkCheckBox(app, text='Elektrik lyuk', width=200, height=30)
luk.place(x=1310, y=290)

sensor_ekran = customtkinter.CTkCheckBox(app, text='Sensor ekran', width=200, height=30)
sensor_ekran.place(x=1310, y=340)

podogrev_sideniy = customtkinter.CTkCheckBox(app, text='Podogrev_sideniy', width=200, height=30)
podogrev_sideniy.place(x=1310, y=390)

kamera_360 = customtkinter.CTkCheckBox(app, text='360 Kamera', width=200, height=30)
kamera_360.place(x=1310, y=440)

avto_parkovka = customtkinter.CTkCheckBox(app, text='Avto parkovka', width=200, height=30)
avto_parkovka.place(x=1310, y=490)
#----------------------------------------------------------------


# ---------------Edited car id====================================================
def getModels():
    models = []
    db = SessionLocal()
    cars = db.query(Car).all()
    for car in cars:
        models.append(car.model)
    return models
#==================================================================================

# ===================== Show info =================================================
def show_notification(title, message):
    root = customtkinter.CTk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, message)  # Display the notification
    root.destroy()
# =================================================================================

edit_car_model_lbl = customtkinter.CTkLabel(app, text="Edit Model", font=custom_font)
edit_car_model_lbl.place(x=600, y=5)

# Engine_size txt box
edit_car_model = customtkinter.CTkComboBox(app, values=getModels(), width=200, height=30)
edit_car_model.place(x=590, y=30)
# ================================================================================



#----------------------- Add images -------------------------------
IMAGES_DIRECTORY = r"C:\Users\-8-\PycharmProjects\tashkent_motors_bot\Images"

def upload_images():
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.webp")]
    )

    if file_paths:
        if not os.path.exists(IMAGES_DIRECTORY):
            status_label.configure(text="Error: 'Images' directory not found!")
            return

        # Create a new unique subdirectory inside "Images"
        global save_directory
        save_directory= os.path.join(IMAGES_DIRECTORY, f"{brand.get("1.0", 'end').strip()}-{model.get("1.0", 'end').strip()}")
        os.makedirs(save_directory)  # Create the new subdirectory

        for file_path in file_paths:
            filename = os.path.basename(file_path)
            dest_path = os.path.join(save_directory, filename)
            shutil.copy(file_path, dest_path)  # Copy images to the new directory
            print(dest_path)

        status_label.configure(text=f"Images saved in: {save_directory}")

img_lbl = customtkinter.CTkLabel(app, text="Add photos", font=custom_font)
img_lbl.place(x=1310, y=540)

status_label = customtkinter.CTkLabel(app, text="No images uploaded")
status_label.place(x=1310, y=620)

# frame = customtkinter.CTkScrollableFrame(master=app, width=500, height=300)
# frame.pack(pady=20, padx=20)

upload_button = customtkinter.CTkButton(master=app, text="Upload Images", command=upload_images)
upload_button.place(x=1310, y=590)

# # Color txt box
# color = customtkinter.CTkTextbox(app, width=200, height=30)
# color.insert("0.0", "Car Color")
# color.place(x=990, y=710)
#-------------------------------------------------------------------------

def add_photos_from_directory(car_id, directory_path):
    db = SessionLocal()

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Create a new CarPhoto entry
            new_photo = CarPhoto(photo_url=file_path, car_id=car_id)
            db.add(new_photo)

    # Commit the transaction
    db.commit()
    db.close()
    print(f"Photos from '{directory_path}' have been added to the database.")

def CreateCar():
    data['brand_data'] = brand.get("1.0", 'end').strip()
    data['model_data'] = model.get("1.0", 'end').strip()
    data['year_data'] = year.get("1.0", 'end').strip()
    data['position_data'] = position.get().strip()
    data['battery_capacity'] = battery_capacity.get("1.0", 'end').strip()
    data['price_data'] = price.get("1.0", 'end').strip()
    data['condition_data'] = condition.get().strip()
    data['body_type_data'] = body_type.get().strip()
    data['engine_type_data'] = engine_type.get().strip()
    data['engine_size_data'] = engine_size.get("1.0", 'end').strip()
    data['horsePower_data'] = horsePower.get("1.0", 'end').strip()
    data['torque_data'] = torque.get("1.0", 'end').strip()
    data['transmission_data'] = transmission.get().strip()
    data['privod_data'] = privod.get().strip()
    data['rasxod_data'] = rasxod.get("1.0", 'end').strip()
    data['uzunligi_data'] = uzunligi.get("1.0", 'end').strip()
    data['balandligi_data'] = balandligi.get("1.0", 'end').strip()
    data['eni_data'] = eni.get("1.0", 'end').strip()
    data['disk_diametr_data'] = disk_diametr.get("1.0", 'end').strip()
    data['clearance_data'] = clearance.get("1.0", 'end').strip()
    data['cargo_capacity_data'] = cargo_capacity.get("1.0", 'end').strip()
    data['seat_capacity_data'] = seat_capacity.get("1.0", 'end').strip()
    data['lift_capacity_data'] = lift_capacity.get("1.0", 'end').strip()
    data['battery_type'] = battery_type.get("1.0", 'end').strip()
    data['probeg_data'] = probeg.get("1.0", 'end').strip()
    data['garantiya_data'] = garantiya.get("1.0", 'end').strip()
    data['color_data'] = color.get("1.0", 'end').strip()
    data['bistr_zaryad'] = bistr_zaryad.get("1.0", 'end').strip()
    data['home_zaryad'] = home_zaryad.get("1.0", 'end').strip()
    data['kond_data'] = kond.get()
    data['cruise_control_data'] = cruise_control.get()
    data['luk_data'] = luk.get()
    data['sensor_ekran_data'] = sensor_ekran.get()
    data['podogrev_sideniy_data'] = podogrev_sideniy.get()
    data['kamera_360_data'] = kamera_360.get()
    data['avto_parkovka_data'] = avto_parkovka.get()

    # print(brand_data, model_data, year_data, position_data, price_data, condition_data, body_type_data, engine_type_data, engine_size_data, horsePower_data, torque_data, transmission_data, privod_data, rasxod_data, uzunligi_data, balandligi_data, eni_data, disk_diametr_data, clearance_data, cargo_capacity_data, seat_capacity_data, lift_capacity_data, probeg_data, garantiya_data, color_data, kond_data, cruise_control_data, luk_data, sensor_ekran_data, podogrev_sideniy_data, kamera_360_data, avto_parkovka_data, sep="\n")

    if data['position_data'] == "":
        data['position_data'] = 0
    if data['battery_capacity'] == "":
        data["battery_capacity"] = 0
    if data['price_data'] == "":
        data['price_data'] = 0
    if data['condition_data'] == "":
        data['condition_data'] = 0
    if data['body_type_data'] == "":
        data['body_type_data'] = 0
    if data['engine_type_data'] == "":
        data['engine_type_data'] = 0
    if data['engine_size_data'] == "":
        data['engine_size_data'] = 0
    if data['horsePower_data'] == "":
        data['horsePower_data'] = 0
    if data['torque_data'] == "":
        data['torque_data'] = 0
    if data['transmission_data'] == "":
        data['transmission_data'] = 0
    if data['privod_data'] == "":
        data['privod_data'] = 0
    if data['rasxod_data'] == "":
        data['rasxod_data'] = 0
    if data['uzunligi_data'] == "":
        data['uzunligi_data'] = 0
    if data['balandligi_data'] == "":
        data['balandligi_data'] = 0
    if data['eni_data'] == "":
        data['eni_data'] = 0
    if data['disk_diametr_data'] == "":
        data['disk_diametr_data'] = 0
    if data['clearance_data'] == "":
        data['clearance_data'] = 0
    if data['cargo_capacity_data'] == "":
        data['cargo_capacity_data'] = 0
    if data['seat_capacity_data'] == "":
        data['seat_capacity_data'] = 0
    if data['lift_capacity_data'] == "":
        data['lift_capacity_data'] = 0
    if data['battery_type'] == "":
        data['battery_type'] = 0
    if data['probeg_data'] == "":
        data['probeg_data'] = 0
    if data['garantiya_data'] == "":
        data['garantiya_data'] = 0
    if data['color_data'] == "":
        data['color_data'] = 0
    if data['bistr_zaryad'] == "":
        data['bistr_zaryad'] = 0
    if data['home_zaryad'] == "":
        data['home_zaryad'] = 0
    if data['kond_data'] == 0:
        data['kond_data'] = 0
    if data['cruise_control_data'] == 0:
        data['cruise_control_data'] = 0
    if data['luk_data'] == 0:
        data['luk_data'] = 0
    if data['sensor_ekran_data'] == 0:
        data['sensor_ekran_data'] = 0
    if data['podogrev_sideniy_data'] == 0:
        data['podogrev_sideniy_data'] = 0
    if data['kamera_360_data'] == 0:
        data['kamera_360_data'] = 0
    if data['avto_parkovka_data'] == 0:
        data['avto_parkovka_data'] = 0

    if data["brand_data"] == "" or data["model_data"] == "" or data["year_data"] == "":
        show_notification("Error", f"Moshina brandi,modeli yoki yili kiritilmadi")
        return

    db = SessionLocal()
    new_car = Car(brand=data['brand_data'], model=data['model_data'], year=data['year_data'], position=data['position_data'],battery_capacity=data["battery_capacity"], price=data['price_data'], condition=data['condition_data'],
                  body_type=data['body_type_data'], engine_type=data['engine_type_data'], engine_size=data['engine_size_data'], horsepower=data['horsePower_data'], torque=data['torque_data'],
                  transmission=data['transmission_data'], privod=data['privod_data'], fuel_spending=data['rasxod_data'], length=data['uzunligi_data'], height=data['balandligi_data'],
                  width=data['eni_data'], disk_diameter=data['disk_diametr_data'], clearance=data['clearance_data'], cargo_capacity=data['cargo_capacity_data'], seat_capacity=data['seat_capacity_data'],
                  lift_capacity=data['lift_capacity_data'], battery_type=data['battery_type'], mileage=data['probeg_data'], guarantee=data['garantiya_data'], color=data['color_data'], bistr_zaryad=data["bistr_zaryad"], home_zaryad=data["home_zaryad"], is_ac_available=data['kond_data'], is_cruise_control_available=data['cruise_control_data'],
                  is_luk_available=data['luk_data'], is_display_available=data['sensor_ekran_data'], is_seat_heat_available=data['podogrev_sideniy_data'], is_360_kamera_available=data['kamera_360_data'], is_auto_parking_available=data['avto_parkovka_data'])

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    add_photos_from_directory(new_car.id, save_directory)

    edit_car_model.set("")
    edit_car_model.configure(values=getModels())



def getData():
    edit_model = edit_car_model.get()
    db = SessionLocal()
    car = db.query(Car).filter(Car.model == edit_model).first()

    if not car:
        print(f"Car with model {edit_model} not found.")
        show_notification("Error", f"Car with this {edit_model} not found")
        db.close()
        return

    brand.delete("1.0", "end")
    brand.insert("end", car.brand)

    model.delete("1.0", "end")
    model.insert("end", car.model)

    year.delete("1.0", "end")
    year.insert("end", car.year)

    position.set("")
    position.set(car.position)

    battery_capacity.delete("1.0", "end")
    battery_capacity.insert("end", car.battery_capacity)

    price.delete("1.0", "end")
    price.insert("end", car.price)

    condition.set("")
    condition.set(car.condition)

    body_type.set("")
    body_type.set(car.body_type)

    engine_type.set("")
    engine_type.set(car.engine_type)

    engine_size.delete("1.0", "end")
    engine_size.insert("end", car.engine_size)

    horsePower.delete("1.0", "end")
    horsePower.insert("end", car.horsepower)

    torque.delete("1.0", "end")
    torque.insert("end", car.torque)

    transmission.set("")
    transmission.set(car.transmission)

    privod.set("")
    privod.set(car.torque)

    rasxod.delete("1.0", "end")
    rasxod.insert("end", car.fuel_spending)

    uzunligi.delete("1.0", "end")
    uzunligi.insert("end", car.length)

    balandligi.delete("1.0", "end")
    balandligi.insert("end", car.height)

    eni.delete("1.0", "end")
    eni.insert("end", car.width)

    disk_diametr.delete("1.0", "end")
    disk_diametr.insert("end", car.disk_diameter)

    clearance.delete("1.0", "end")
    clearance.insert("end", car.clearance)

    cargo_capacity.delete("1.0", "end")
    cargo_capacity.insert("end", car.cargo_capacity)

    seat_capacity.delete("1.0", "end")
    seat_capacity.insert("end", car.seat_capacity)

    lift_capacity.delete("1.0", "end")
    lift_capacity.insert("end", car.lift_capacity)

    battery_type.delete("1.0", "end")
    battery_type.insert("end", car.battery_type)

    probeg.delete("1.0", "end")
    probeg.insert("end", car.mileage)

    probeg.delete("1.0", "end")
    probeg.insert("end", car.mileage)

    garantiya.delete("1.0", "end")
    garantiya.insert("end", car.guarantee)

    color.delete("1.0", "end")
    color.insert("end", car.color)

    bistr_zaryad.delete("1.0", "end")
    bistr_zaryad.insert("end", car.bistr_zaryad)

    home_zaryad.delete("1.0", "end")
    home_zaryad.insert("end", car.home_zaryad)

    kond.deselect()
    cruise_control.deselect()
    luk.deselect()
    sensor_ekran.deselect()
    podogrev_sideniy.deselect()
    kamera_360.deselect()
    avto_parkovka.deselect()


def EditCarData():
    data['brand_data'] = brand.get("1.0", 'end').strip()
    data['model_data'] = model.get("1.0", 'end').strip()
    data['year_data'] = year.get("1.0", 'end').strip()
    data['position_data'] = position.get().strip()
    data['battery_capacity'] = battery_capacity.get("1.0", 'end').strip()
    data['price_data'] = price.get("1.0", 'end').strip()
    data['condition_data'] = condition.get().strip()
    data['body_type_data'] = body_type.get().strip()
    data['engine_type_data'] = engine_type.get().strip()
    data['engine_size_data'] = engine_size.get("1.0", 'end').strip()
    data['horsePower_data'] = horsePower.get("1.0", 'end').strip()
    data['torque_data'] = torque.get("1.0", 'end').strip()
    data['transmission_data'] = transmission.get().strip()
    data['privod_data'] = privod.get().strip()
    data['rasxod_data'] = rasxod.get("1.0", 'end').strip()
    data['uzunligi_data'] = uzunligi.get("1.0", 'end').strip()
    data['balandligi_data'] = balandligi.get("1.0", 'end').strip()
    data['eni_data'] = eni.get("1.0", 'end').strip()
    data['disk_diametr_data'] = disk_diametr.get("1.0", 'end').strip()
    data['clearance_data'] = clearance.get("1.0", 'end').strip()
    data['cargo_capacity_data'] = cargo_capacity.get("1.0", 'end').strip()
    data['seat_capacity_data'] = seat_capacity.get("1.0", 'end').strip()
    data['lift_capacity_data'] = lift_capacity.get("1.0", 'end').strip()
    data['battery_type'] = battery_type.get("1.0", 'end').strip()
    data['probeg_data'] = probeg.get("1.0", 'end').strip()
    data['garantiya_data'] = garantiya.get("1.0", 'end').strip()
    data['color_data'] = color.get("1.0", 'end').strip()
    data['bistr_zaryad'] = bistr_zaryad.get("1.0", 'end').strip()
    data['home_zaryad'] = home_zaryad.get("1.0", 'end').strip()
    data['kond_data'] = kond.get()
    data['cruise_control_data'] = cruise_control.get()
    data['luk_data'] = luk.get()
    data['sensor_ekran_data'] = sensor_ekran.get()
    data['podogrev_sideniy_data'] = podogrev_sideniy.get()
    data['kamera_360_data'] = kamera_360.get()
    data['avto_parkovka_data'] = avto_parkovka.get()

    # print(brand_data, model_data, year_data, position_data, price_data, condition_data, body_type_data, engine_type_data, engine_size_data, horsePower_data, torque_data, transmission_data, privod_data, rasxod_data, uzunligi_data, balandligi_data, eni_data, disk_diametr_data, clearance_data, cargo_capacity_data, seat_capacity_data, lift_capacity_data, probeg_data, garantiya_data, color_data, kond_data, cruise_control_data, luk_data, sensor_ekran_data, podogrev_sideniy_data, kamera_360_data, avto_parkovka_data, sep="\n")

    if data['position_data'] == "":
        data['position_data'] = 0
    if data['battery_capacity'] == "":
        data["battery_capacity"] = 0
    if data['price_data'] == "":
        data['price_data'] = 0
    if data['condition_data'] == "":
        data['condition_data'] = 0
    if data['body_type_data'] == "":
        data['body_type_data'] = 0
    if data['engine_type_data'] == "":
        data['engine_type_data'] = 0
    if data['engine_size_data'] == "":
        data['engine_size_data'] = 0
    if data['horsePower_data'] == "":
        data['horsePower_data'] = 0
    if data['torque_data'] == "":
        data['torque_data'] = 0
    if data['transmission_data'] == "":
        data['transmission_data'] = 0
    if data['privod_data'] == "":
        data['privod_data'] = 0
    if data['rasxod_data'] == "":
        data['rasxod_data'] = 0
    if data['uzunligi_data'] == "":
        data['uzunligi_data'] = 0
    if data['balandligi_data'] == "":
        data['balandligi_data'] = 0
    if data['eni_data'] == "":
        data['eni_data'] = 0
    if data['disk_diametr_data'] == "":
        data['disk_diametr_data'] = 0
    if data['clearance_data'] == "":
        data['clearance_data'] = 0
    if data['cargo_capacity_data'] == "":
        data['cargo_capacity_data'] = 0
    if data['seat_capacity_data'] == "":
        data['seat_capacity_data'] = 0
    if data['lift_capacity_data'] == "":
        data['lift_capacity_data'] = 0
    if data['battery_type'] == "":
        data['battery_type'] = 0
    if data['probeg_data'] == "":
        data['probeg_data'] = 0
    if data['garantiya_data'] == "":
        data['garantiya_data'] = 0
    if data['color_data'] == "":
        data['color_data'] = 0
    if data['bistr_zaryad'] == "":
        data['bistr_zaryad'] = 0
    if data['home_zaryad'] == "":
        data['home_zaryad'] = 0
    if data['kond_data'] == 0:
        data['kond_data'] = 0
    if data['cruise_control_data'] == 0:
        data['cruise_control_data'] = 0
    if data['luk_data'] == 0:
        data['luk_data'] = 0
    if data['sensor_ekran_data'] == 0:
        data['sensor_ekran_data'] = 0
    if data['podogrev_sideniy_data'] == 0:
        data['podogrev_sideniy_data'] = 0
    if data['kamera_360_data'] == 0:
        data['kamera_360_data'] = 0
    if data['avto_parkovka_data'] == 0:
        data['avto_parkovka_data'] = 0

    edit_model = edit_car_model.get()
    db = SessionLocal()
    car = db.query(Car).filter(Car.model == edit_model).first()

    if not car:
        print(f"Car with model {edit_model} not found.")
        show_notification("Error", f"Car with this {edit_model} not found")
        db.close()
        return

    car.brand = data['brand_data']
    car.model = data['model_data']
    car.year = data['year_data']
    car.position=data['position_data']
    car.battery_capacity=data["battery_capacity"]
    car.price=data['price_data']
    car.condition=data['condition_data']
    car.body_type=data['body_type_data']
    car.engine_type=data['engine_type_data']
    car.engine_size=data['engine_size_data']
    car.horsepower=data['horsePower_data']
    car.torque=data['torque_data']
    car.transmission=data['transmission_data']
    car.privod=data['privod_data']
    car.fuel_spending=data['rasxod_data']
    car.length=data['uzunligi_data']
    car.width=data['eni_data']
    car.disk_diameter=data['disk_diametr_data']
    car.clearance=data['clearance_data']
    car.cargo_capacity=data['cargo_capacity_data']
    car.seat_capacity=data['seat_capacity_data']
    car.lift_capacity=data['lift_capacity_data']
    car.battery_type=data['battery_type']
    car.mileage=data['probeg_data']
    car.guarantee=data['garantiya_data']
    car.color=data['color_data']
    car.bistr_zaryad=data["bistr_zaryad"]
    car.home_zaryad=data["home_zaryad"]
    car.is_ac_available=data['kond_data']
    car.is_cruise_control_available=data['cruise_control_data']
    car.is_luk_available=data['luk_data']
    car.is_display_available=data['sensor_ekran_data']
    car.is_seat_heat_available=data['podogrev_sideniy_data']
    car.is_360_kamera_available=data['kamera_360_data']
    car.is_auto_parking_available=data['avto_parkovka_data']

    db.commit()
    db.refresh(car)
    db.close()

    add_photos_from_directory(car.id, save_directory)

    edit_car_model.set("")
    edit_car_model.configure(values=getModels())

#============================Delete the Car====================================
def DeleteCarData():
    db = SessionLocal()
    edit_model = edit_car_model.get()
    car = db.query(Car).filter(Car.model == edit_model).first()

    if not car:
        print(f"Car with model {edit_model} not found.")
        show_notification("Error", f"Car with this {edit_model} not found")
        db.close()
        return

    db.query(CarPhoto).filter(CarPhoto.car_id == car.id).delete()

    db.delete(car)
    db.commit()
    db.close()

    edit_car_model.set("")
    edit_car_model.configure(values=getModels())
    print(f"Car with model {edit_model} has been deleted.")


#----------------------------- Buttons--------------------------------
add_button = customtkinter.CTkButton(app, text="Add Car", command=CreateCar)
add_button.place(x=100, y=30)

get_button = customtkinter.CTkButton(app, text="Get Car Data", command=getData)
get_button.place(x=400, y=30)

edit_button2 = customtkinter.CTkButton(app, text="Edit Car", command=EditCarData)
edit_button2.place(x=830, y=30)

delete_car = customtkinter.CTkButton(app, text="Delete Car", command=DeleteCarData)
delete_car.place(x=1000, y=30)
#============================================================================


# Run the application
app.mainloop()