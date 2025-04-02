from utils import get_Car_Spicifications


ac = "not identified"
cruise_c = "not identified"
luk = "not identified"
ekran = "not identified"
podogrev_sid = "not identified"
kamera_360_gradus = "not identified"
auto_parkovka = "not identified"

txt = ""
# final_txt = ""
spec = {}
def getCarSpecifications(model):
    comforts_list = []
    specifications = get_Car_Spicifications.get_car_by_model_filtered(model)
    print(specifications)
    if specifications["brand"] != "0":
        spec["🔰🔰Brand:             "] = specifications["brand"]
    if specifications["model"] != "0":
        spec["🚘🚘Model:             "] = specifications["model"]
    if specifications["year"] != "0":
        spec["📆📆Yil:               "] = specifications["year"]
    if specifications["price"] != "0":
        spec["💰💵Narxi:             "] = specifications["price"]
    if specifications["position"] != "0":
        spec["🎚️🎚️Pozitsiya:         "] = specifications["position"]
    if specifications["battery_capacity"] != "0":
        spec["🔋⚡Batareya sig'imi:  "] = specifications["battery_capacity"]
    if specifications["condition"] != "0":
        spec["✅✅Holati:            "] = specifications["condition"]
    if specifications["body_type"] != "0":
        spec["🚗🚙Kuzov turi:        "] = specifications["body_type"]
    if specifications["engine_type"] != "0":
        spec["⛽⛽Yoqilg'i turi:     "] = specifications["engine_type"]
    if specifications["engine_size"] != "0":
        spec["⚙️📏Dvigatel hajmi:    "] = specifications["engine_size"]
    if specifications["horsepower"] != "0":
        spec["🐎⚡Ot kuchi:          "] = specifications["horsepower"]
    if specifications["transmission"] != "0":
        spec["⚙️🔀Transmissiya:      "] = specifications["transmission"]
    if specifications["fuel_spending"] != "0":
        spec["⛽📉Yoqilg'i sarfi:    "] = specifications["fuel_spending"]
    if specifications["length"] != "0":
        spec["📏➡️Uzunligi:          "] = specifications["length"]
    if specifications["height"] != "0":
        spec["📏⬆️Balandligi:        "] = specifications["height"]
    if specifications["width"] != "0":
        spec["📏↔️Eni:               "] = specifications["width"]
    if specifications["disk_diameter"] != "0":
        spec["⚫📏Diska diametri:    "] = specifications["disk_diameter"]
    if specifications["clearance"] != "0":
        spec["↕️↕️Yerdan balandligi"] = specifications["clearance"]
    if specifications["cargo_capacity"] != "0":
        spec["📦🚗Bagaj sig'imi:     "] = specifications["cargo_capacity"]
    if specifications["lift_capacity"] != "0":
        spec["🏋️💪Yuk ko'tarishi:"] = specifications["lift_capacity"]
    if specifications["seat_capacity"] != "0":
        spec["🪑🚘O'rindiqlar soni:  "] = specifications["seat_capacity"]
    if specifications["mileage"] != "0":
        spec["📍🚗Probeg:"] = specifications["probeg"]
    if specifications["battery_type"] != "0":
        spec["🔋🧪Batareya turi:     "] = specifications["battery_type"]
    if specifications["guarantee"] != "0":
        spec["🛡️📜Garantiya:         "] = specifications["guarantee"]
    if specifications["color"] != "0":
        spec["🎨🚗Rangi:             "] = specifications["color"]

    if specifications["is_ac_available"]:
        global ac
        ac = "✅✅Konditsioner"
        comforts_list.append(ac)
    else:
        ac = ""
    if specifications["is_cruise_control_available"]:
        global cruise_c
        cruise_c = "✅✅Kruiz kontrol"
        comforts_list.append(cruise_c)
    else:
        cruise_c = ""
    if specifications["is_luk_available"]:
        global luk
        luk = "✅✅Panarama Elektrik luk"
        comforts_list.append(luk)
    else:
        luk = ""
    if specifications["is_display_available"]:
        global ekran
        ekran = "✅✅Sensor Ekran"
        comforts_list.append(ekran)
    else:
        ekran = ""
    if specifications["is_seat_heat_available"]:
        global podogrev_sid
        podogrev_sid = "✅✅O'rindiqlar isishi"
        comforts_list.append(podogrev_sid)
    else:
        podogrev_sid = ""
    if specifications["is_360_kamera_available"]:
        global kamera_360_gradus
        kamera_360_gradus = "✅✅360 Kamera"
        comforts_list.append(kamera_360_gradus)
    else:
        kamera_360_gradus = ""
    if specifications["is_auto_parking_available"]:
        global auto_parkovka
        auto_parkovka = "✅✅Avto parkovka"
        comforts_list.append(auto_parkovka)
    else:
        auto_parkovka = ""

    formatted_lines = [f"{key}{value}" for key, value in spec.items()]
    final_txt = "\n".join(formatted_lines) + "\n\n" + "\n".join(comforts_list)
    return f"\n{final_txt}\n"
