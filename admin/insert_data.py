from tkinter import filedialog
from PIL import Image

import customtkinter

# Create the main window
app = customtkinter.CTk()
app.geometry("1500x900")
app.title("Add car")

custom_font = customtkinter.CTkFont(family="Arial", size=14, weight="bold")

#--------------------- car brand -------------------------------
# brand label
brand_lbl = customtkinter.CTkLabel(app, text="Brand", font=custom_font)
brand_lbl.place(x=100, y=80)

# brand text box
brand = customtkinter.CTkTextbox(app, width=200, height=30)
brand.insert("0.0", "Brand of the car")
brand.place(x=90, y=110)
#---------------------------------------------------------------

#---------------------car model-------------------------------
# model label
model_lbl = customtkinter.CTkLabel(app, text="Model", font=custom_font)
model_lbl.place(x=400, y=80)

# model txt box
model = customtkinter.CTkTextbox(app, width=200, height=30)
model.insert("0.0", "Model of the car")
model.place(x=390, y=110)
#----------------------------------------------------------------

#---------------------car year-------------------------------
# year label
year_lbl = customtkinter.CTkLabel(app, text="Year", font=custom_font)
year_lbl.place(x=700, y=80)

# year txt box
year = customtkinter.CTkTextbox(app, width=200, height=30)
year.insert("0.0", "Year of the car")
year.place(x=690, y=110)
#----------------------------------------------------------------

#---------------------car position-------------------------------
# position label
position_lbl = customtkinter.CTkLabel(app, text="Position", font=custom_font)
position_lbl.place(x=1000, y=80)

# position txt box
position = customtkinter.CTkComboBox(app, values=['1chi pozitsiya', '2chi pozitsiya', '3chi pozitsiya'], width=200, height=30)
position.place(x=990, y=110)
#----------------------------------------------------------------

#---------------------car Price-------------------------------
# Price label
price_lbl = customtkinter.CTkLabel(app, text="Price", font=custom_font)
price_lbl.place(x=100, y=200)

# Price txt box
price = customtkinter.CTkTextbox(app, width=200, height=30)
price.insert("0.0", "Price of the car")
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
engine_type_lbl.place(x=700, y=200)

# Engine type box
engine_type = customtkinter.CTkComboBox(app, values=['Benzin', 'Dizel', 'Elektr', 'Gibrid'], width=200, height=30)
engine_type.place(x=690, y=230)
#----------------------------------------------------------------

#---------------------car Engine size-------------------------------
# Engine size label
engine_size_lbl = customtkinter.CTkLabel(app, text="Engine type", font=custom_font)
engine_size_lbl.place(x=1000, y=200)

# Engine_size txt box
engine_size = customtkinter.CTkTextbox(app, width=200, height=30)
engine_size.insert("0.0", "Engine size of the car")
engine_size.place(x=990, y=230)
#----------------------------------------------------------------

#---------------------car HorsePower-------------------------------
# HorsePower label
horsePower_lbl = customtkinter.CTkLabel(app, text="HorsePower", font=custom_font)
horsePower_lbl.place(x=100, y=320)

# HorsePower txt box
horsePower = customtkinter.CTkTextbox(app, width=200, height=30)
horsePower.insert("0.0", "HorsePower of the car")
horsePower.place(x=90, y=350)
#----------------------------------------------------------------

#---------------------car Torque-------------------------------
# Torque label
torque_lbl = customtkinter.CTkLabel(app, text="Torque", font=custom_font)
torque_lbl.place(x=400, y=320)

# Torque txt box
torque = customtkinter.CTkTextbox(app, width=200, height=30)
torque.insert("0.0", "Torque of the car")
torque.place(x=390, y=350)
#----------------------------------------------------------------

#---------------------car Transmission-------------------------------
# Transmission label
transmission_lbl = customtkinter.CTkLabel(app, text="Transmission", font=custom_font)
transmission_lbl.place(x=700, y=320)

# Transmission txt box
transmission = customtkinter.CTkComboBox(app, values=['Avtomat', 'Mexanik', 'Robot', 'Variator'], width=200, height=30)
transmission.place(x=690, y=350)
#----------------------------------------------------------------

#---------------------car Privod-------------------------------
# Privod label
privod_lbl = customtkinter.CTkLabel(app, text="Privod", font=custom_font)
privod_lbl.place(x=1000, y=320)

# Privod txt box
privod = customtkinter.CTkComboBox(app, values=['Oldi', 'Orqa', '4 tomon'], width=200, height=30)
privod.place(x=990, y=350)
#----------------------------------------------------------------

#---------------------car Rasxod-------------------------------
# Rasxod label
rasxod_lbl = customtkinter.CTkLabel(app, text="Rasxod", font=custom_font)
rasxod_lbl.place(x=100, y=440)

# Rasxod txt box
rasxod = customtkinter.CTkTextbox(app, width=200, height=30)
rasxod.insert("0.0", "Moshina rasxodi")
rasxod.place(x=90, y=470)
#----------------------------------------------------------------

#---------------------car Uzunligi-------------------------------
# Uzunligi label
uzunligi_lbl = customtkinter.CTkLabel(app, text="Uzunligi", font=custom_font)
uzunligi_lbl.place(x=400, y=440)

# Uzunligi txt box
uzunligi = customtkinter.CTkTextbox(app, width=200, height=30)
uzunligi.insert("0.0", "Moshina Uzunligi")
uzunligi.place(x=390, y=470)
#----------------------------------------------------------------

#---------------------car Balandligi-------------------------------
# Balandligi label
balandligi_lbl = customtkinter.CTkLabel(app, text="Balandligi", font=custom_font)
balandligi_lbl.place(x=700, y=440)

# Balandligi txt box
balandligi = customtkinter.CTkTextbox(app, width=200, height=30)
balandligi.insert("0.0", "Moshina Balandligi")
balandligi.place(x=690, y=470)
#----------------------------------------------------------------

#---------------------car Eni-------------------------------
# Eni label
eni_lbl = customtkinter.CTkLabel(app, text="Eni", font=custom_font)
eni_lbl.place(x=1000, y=440)

# Eni txt box
eni = customtkinter.CTkTextbox(app, width=200, height=30)
eni.insert("0.0", "Moshina Eni")
eni.place(x=990, y=470)
#----------------------------------------------------------------

#---------------------car Diska diametri-------------------------------
# Diska diametri label
disk_diametr_lbl = customtkinter.CTkLabel(app, text="Diska diametri", font=custom_font)
disk_diametr_lbl.place(x=100, y=560)

# Diska diametri txt box
disk_diametr = customtkinter.CTkTextbox(app, width=200, height=30)
disk_diametr.insert("0.0", "Moshina Diska diametri")
disk_diametr.place(x=90, y=590)
#----------------------------------------------------------------

#---------------------car Clearance-------------------------------
# Clearance label
clearance_lbl = customtkinter.CTkLabel(app, text="Clearance", font=custom_font)
clearance_lbl.place(x=400, y=560)

# Clearance txt box
clearance = customtkinter.CTkTextbox(app, width=200, height=30)
clearance.insert("0.0", "Car Clearance")
clearance.place(x=390, y=590)
#----------------------------------------------------------------

#---------------------car Cargo Capacity-------------------------------
# Cargo Capacity label
cargo_capacity_lbl = customtkinter.CTkLabel(app, text="Cargo Capacity", font=custom_font)
cargo_capacity_lbl.place(x=700, y=560)

# Cargo Capacity txt box
cargo_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
cargo_capacity.insert("0.0", "Car Cargo Capacity")
cargo_capacity.place(x=690, y=590)
#----------------------------------------------------------------

#---------------------car Seat Capacity-------------------------------
# Seat Capacity label
seat_capacity_lbl = customtkinter.CTkLabel(app, text="Seat Capacity", font=custom_font)
seat_capacity_lbl.place(x=1000, y=560)

# Seat Capacity txt box
seat_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
seat_capacity.insert("0.0", "Car Seat Capacity")
seat_capacity.place(x=990, y=590)
#----------------------------------------------------------------

#---------------------car Lifting Capacity-------------------------------
# Lifting Capacity label
lift_capacity_lbl = customtkinter.CTkLabel(app, text="Lifting Capacity", font=custom_font)
lift_capacity_lbl.place(x=100, y=680)

# Lifting Capacity txt box
lift_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
lift_capacity.insert("0.0", "Car Lifting Capacity")
lift_capacity.place(x=90, y=710)
#----------------------------------------------------------------

#---------------------car Lifting Capacity-------------------------------
# Lifting Capacity label
lift_capacity_lbl = customtkinter.CTkLabel(app, text="Lifting Capacity", font=custom_font)
lift_capacity_lbl.place(x=100, y=680)

# Lifting Capacity txt box
lift_capacity = customtkinter.CTkTextbox(app, width=200, height=30)
lift_capacity.insert("0.0", "Car Lifting Capacity")
lift_capacity.place(x=90, y=710)
#----------------------------------------------------------------

#---------------------car Probeg-------------------------------
# Probeg label
probeg_lbl = customtkinter.CTkLabel(app, text="Probeg", font=custom_font)
probeg_lbl.place(x=400, y=680)

# Probeg txt box
probeg = customtkinter.CTkTextbox(app, width=200, height=30)
probeg.insert("0.0", "Car Probeg")
probeg.place(x=390, y=710)
#----------------------------------------------------------------

#---------------------car Garantiya-------------------------------
# Garantiya label
garantiya_lbl = customtkinter.CTkLabel(app, text="Garantiya", font=custom_font)
garantiya_lbl.place(x=700, y=680)

# Garantiya txt box
garantiya = customtkinter.CTkTextbox(app, width=200, height=30)
garantiya.insert("0.0", "Car Garantiya")
garantiya.place(x=690, y=710)
#----------------------------------------------------------------

#---------------------car Color-------------------------------
# Color label
color_lbl = customtkinter.CTkLabel(app, text="Color", font=custom_font)
color_lbl.place(x=1000, y=680)

# Color txt box
color = customtkinter.CTkTextbox(app, width=200, height=30)
color.insert("0.0", "Car Color")
color.place(x=990, y=710)
#----------------------------------------------------------------

#---------------------car Features-------------------------------
kond = customtkinter.CTkCheckBox(app, text='Konditsioner', width=200, height=30)
kond.place(x=1310, y=110)

cruise_control = customtkinter.CTkCheckBox(app, text="Adaptive kruiz kontrol", width=200, height=30)
cruise_control.place(x=1310, y=160)

luk = customtkinter.CTkCheckBox(app, text='Elektrik lyuk', width=200, height=30)
luk.place(x=1310, y=210)

sensor_ekran = customtkinter.CTkCheckBox(app, text='Sensor ekran', width=200, height=30)
sensor_ekran.place(x=1310, y=260)

podogrev_sideniy = customtkinter.CTkCheckBox(app, text='Podogrev_sideniy', width=200, height=30)
podogrev_sideniy.place(x=1310, y=310)

kamera_360 = customtkinter.CTkCheckBox(app, text='360 Kamera', width=200, height=30)
kamera_360.place(x=1310, y=360)

avto_parkovka = customtkinter.CTkCheckBox(app, text='Avto parkovka', width=200, height=30)
avto_parkovka.place(x=1310, y=410)
#----------------------------------------------------------------

#----------------------- Add images -------------------------------
def upload_images():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_paths:
        for idx, file_path in enumerate(file_paths):
            img = customtkinter.CTkImage(light_image=Image.open(file_path), size=(100, 100))
            label = customtkinter.CTkLabel(master=app, image=img, text="")
            label.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)
            label.image = img

img_lbl = customtkinter.CTkLabel(app, text="Add photos", font=custom_font)
img_lbl.place(x=1310, y=450)

# frame = customtkinter.CTkScrollableFrame(master=app, width=500, height=300)
# frame.pack(pady=20, padx=20)

upload_button = customtkinter.CTkButton(master=app, text="Upload Images", command=upload_images)
upload_button.place(x=1310, y=500)

# Color txt box
color = customtkinter.CTkTextbox(app, width=200, height=30)
color.insert("0.0", "Car Color")
color.place(x=990, y=710)
#-------------------------------------------------------------------------


button = customtkinter.CTkButton(app, text="Click Me")
button.pack(pady=20)

# Run the application
app.mainloop()