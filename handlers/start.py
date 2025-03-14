from aiogram import Router, F, types
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                                 CallbackQuery)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import datetime
from dotenv import load_dotenv
import os

from create_bot import bot
from utils import get_Car_Spicifications

from keyboards.Keys import main_keyboard, cars_keyboard, filial_keyboard, get_car_brands_inline, get_car_models_inline, get_car_options_inline

load_dotenv()
start_router = Router()


model = ""
ac = "not identified"
cruise_c = "not identified"
luk = "not identified"
ekran = "not identified"
podogrev_sid = "not identified"
kamera_360_gradus = "not identified"
auto_parkovka = "not identified"
comforts_list = []

# Define states for user input
class RequestState(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()

# Car shop details
SHOP_NAME = os.getenv("SHOP_NAME")
SHOP_ADDRESS = os.getenv("SHOP_ADDRESS")
WORKING_HOURS = os.getenv("WORKING_HOURS")
SHOP_LATITUDE = os.getenv("SHOP_LATITUDE")
SHOP_LONGITUDE = os.getenv("SHOP_LONGITUDE")
#===========================================================

# Manager details
NAME = os.getenv("NAME")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
TG_USERNAME = os.getenv("TG_USERNAME")

# group chat id
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")


# Car brands and their models
# car_brands = {
#     "Toyota": ["Camry", "Corolla", "Land Cruiser"],
#     "BMW": ["X5", "M3", "i8"],
#     "Mercedes": ["E-Class", "C-Class", "GLS"]
# }

# Handler for "Cars" button
@start_router.message(lambda message: message.text == "🚗Avtomobillar")
async def cars_handler(message: types.Message):
    text = "Avtomobil turini tanlang: "
    await message.answer(text, reply_markup=cars_keyboard)

@start_router.message(lambda message: message.text == "🚗Yengil avtomobillar")
async def yengil_avto_handler(message: types.Message):
    text = "🚗Avtomobil brandini tanlang:"
    await message.answer(text, reply_markup=get_car_brands_inline())

@start_router.message(lambda message: message.text == "🚚Yuk avtomobillar")
async def yuk_avto_handler(message: types.Message):
    text = "🚚Yuk avtomobillar:"
    await message.answer(text, reply_markup=get_car_brands_inline())

# Handler to go back to the main menu
@start_router.message(lambda message: message.text == "🔙 Orqaga")
async def back_to_main_menu(message: types.Message):
    text = "🏠 Bosh menu:"
    await message.answer(text, reply_markup=main_keyboard)
#======================================================================================

# Handling inline button presses for car brands (show models)
@start_router.callback_query(F.data.startswith("brand_"))
async def car_brand_handler(call: CallbackQuery):
    brand = call.data.split("_")[1]  # Extract brand name
    await call.message.answer(f"🚘 {brand} models:", reply_markup=get_car_models_inline(brand))

# Handling inline button presses for car models
@start_router.callback_query(F.data.startswith("model_"))
async def car_model_handler(call: CallbackQuery, state: FSMContext):
    global model
    model = call.data.split("_")[1]  # Extract model name
    await state.update_data(car_model=model)
    await call.message.answer(f"🚘 {model} xarakteristikasi...\n\nIltmos tanlang:", reply_markup=get_car_options_inline())

# Handler for "Back" button inside car models (returns to brands)
@start_router.callback_query(F.data == "back_to_brands")
async def back_to_brands(call: CallbackQuery):
    await call.message.answer("🚗 Please choose a brand:", reply_markup=get_car_brands_inline())


# Handler for "Back" button inside inline car list
@start_router.callback_query(F.data == "back_to_cars")
async def back_to_cars(call: CallbackQuery):
    await call.message.answer("🚗 Please choose a category:", reply_markup=cars_keyboard)

# Handler for "Leave the request" button (asks for user's name)
@start_router.callback_query(F.data == "leave_request")
async def leave_request_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("📝 Please enter your full name:")
    await state.set_state(RequestState.waiting_for_name)

# Handler for user sending their name
@start_router.message(RequestState.waiting_for_name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📞 Now, please share your phone number.",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[[KeyboardButton(text="📲 Share My Number", request_contact=True)]],
                             resize_keyboard=True, one_time_keyboard=True
                         ))
    await state.set_state(RequestState.waiting_for_phone)

# Handler for user sending their phone number
@start_router.message(RequestState.waiting_for_phone, F.contact)
async def get_user_phone(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data["name"]
    phone = message.contact.phone_number
    car_model = user_data["car_model"]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    group_message = (
        f"📩 New Car Request!\n"
        f"👤 Name: {name}\n"
        f"📞 Phone: {phone}\n"
        f"🚘 Interested in: {car_model}\n"
        f"⏰ Time: {timestamp}"
    )
    await message.bot.send_message(GROUP_CHAT_ID, group_message)

    # Confirming to the user
    await message.answer("✅ Your request has been recorded and sent to our team!", reply_markup=main_keyboard)

    await state.clear()

@start_router.callback_query(F.data == "contact_manager")
async def contact_manager_handler(call: CallbackQuery):
    manager_info = "👨‍💼 Manager Contact:\n📞 +998909528282\n📩 Telegram: @temurbek_tashkent_motors"
    await call.message.answer(manager_info)

# Car specifications
@start_router.callback_query(F.data == "car specifications")
async def car_specifications(call: CallbackQuery, state: FSMContext):
    specifications = get_Car_Spicifications.get_car_by_model_filtered(model)
    specifications["probeg"] = "0"
    if specifications["engine_type"] == "Benzin":
        if specifications["is_ac_available"]:
            global ac
            ac = "✅Konditsioner"
            comforts_list.append(ac)
        else:
            ac = ""
        if specifications["is_cruise_control_available"]:
            global cruise_c
            cruise_c = "✅Kruiz kontrol"
            comforts_list.append(cruise_c)
        else:
            cruise_c = ""
        if specifications["is_luk_available"]:
            global luk
            luk = "✅Panarama Elektrik luk"
            comforts_list.append(luk)
        else:
            luk = ""
        if specifications["is_display_available"]:
            global ekran
            ekran = "✅Sensor Ekran"
            comforts_list.append(ekran)
        else:
            ekran = ""
        if specifications["is_seat_heat_available"]:
            global podogrev_sid
            podogrev_sid = "✅O'rindiqlar isishi"
            comforts_list.append(podogrev_sid)
        else:
            podogrev_sid = ""
        if specifications["is_360_kamera_available"]:
            global kamera_360_gradus
            kamera_360_gradus = "✅360 Kamera"
            comforts_list.append(kamera_360_gradus)
        else:
            kamera_360_gradus = ""
        if specifications["is_auto_parking_available"]:
            global auto_parkovka
            auto_parkovka = "✅Avto parkovka"
            comforts_list.append(auto_parkovka)
        else:
            auto_parkovka = ""
        print(comforts_list)
        await call.message.answer(f"<pre>"
                                  f"🔰🔰Brand:            <b>{specifications["brand"]}</b>\n"
                                  f"🚘🚘Model:            <b>{specifications["model"]}</b>\n"
                                  f"📆📆Yil:              <b>{specifications["year"]}</b>\n"
                                  f"💰💵Narxi:            <b>{specifications["price"]}</b>\n"
                                  f"✅✅Holati:           <b>{specifications["condition"]}</b>\n"
                                  f"🚗🚙Kuzov turi:       <b>{specifications["body_type"]}</b>\n"
                                  f"⛽⛽Yoqilg'i turi:    <b>{specifications["engine_type"]}</b>\n"
                                  f"⚙️📏Dvigatel hajmi:   <b>{specifications["engine_size"]} litr</b>\n"
                                  f"🐎⚡Ot kuchi:          <b>{specifications["horsepower"]}</b>\n"
                                  f"⚙️🔀Transmissiya:     <b>{specifications["transmission"]}</b>\n"
                                  f"⛽📉Yoqilg'i sarfi:   <b>{specifications["fuel_spending"]} litr/100km</b>\n"
                                  f"📏➡️Uzunligi:         <b>{specifications["length"]} mm</b>\n"
                                  f"📏⬆️Balandligi:       <b>{specifications["height"]} mm</b>\n"
                                  f"📏↔️Eni:              <b>{specifications["width"]} mm</b>\n"
                                  f"⚫📏Diska diametri:   <b>{specifications["disk_diameter"]} dyum</b>\n"
                                  f"📦🚗Bagaj sig'imi:    <b>{specifications["cargo_capacity"]} litr</b>\n"
                                  f"🪑🚘O'rindiqlar soni: <b>{specifications["seat_capacity"]}</b>\n"
                                  f"📍🚗Probeg:           <b>{specifications["probeg"]}</b>\n"
                                  f"🛡️📜Garantiya:        <b>{specifications["guarantee"]}</b>\n"
                                  f"🎨🚗Rangi:            <b>{specifications["color"]}</b>\n"
                                  f"</pre>",
                                    parse_mode="HTML")
        await call.message.answer("\n".join(comforts_list))

    elif specifications["engine_type"] == "Elektr":
        if specifications["is_ac_available"]:
            ac = "✅Konditsioner"
            comforts_list.append(ac)
        else:
            ac = ""
        if specifications["is_cruise_control_available"]:
            cruise_c = "✅Kruiz kontrol"
            comforts_list.append(cruise_c)
        else:
            cruise_c = ""
        if specifications["is_luk_available"]:
            luk = "✅Panarama Elektrik luk"
            comforts_list.append(luk)
        else:
            luk = ""
        if specifications["is_display_available"]:
            ekran = "✅Sensor Ekran"
            comforts_list.append(ekran)
        else:
            ekran = ""
        if specifications["is_seat_heat_available"]:
            podogrev_sid = "✅O'rindiqlar isishi"
            comforts_list.append(podogrev_sid)
        else:
            podogrev_sid = ""
        if specifications["is_360_kamera_available"]:
            kamera_360_gradus = "✅360 Kamera"
            comforts_list.append(kamera_360_gradus)
        else:
            kamera_360_gradus = ""
        if specifications["is_auto_parking_available"]:
            auto_parkovka = "✅Avto parkovka"
            comforts_list.append(auto_parkovka)
        else:
            auto_parkovka = None
        await call.message.answer(f"<pre>"
                                  f"🔰🔰Brand:                      <b>{specifications["brand"]}</b>\n"
                                  f"🚘🚘Model:                      <b>{specifications["model"]}</b>\n"
                                  f"📆📆Yil:                        <b>{specifications["year"]}</b>\n"
                                  f"💰💵Narxi:                      <b>{specifications["price"]} $</b>\n"
                                  f"✅✅Holati:                     <b>{specifications["condition"]}</b>\n"
                                  f"🔋⚡Batareya sig'imi:           <b>{specifications["battery_capacity"]} kWatt/soat</b>\n"
                                  f"⚡🚀Tez zaryad olish vaqti:     <b>{specifications["bistr_zaryad"]}</b>\n"
                                  f"🏠🔌Uyda zaryad olish vaqti:    <b>{specifications["home_zaryad"]}</b>\n"
                                  f"🚗🚙Kuzov turi:                 <b>{specifications["body_type"]}</b>\n"
                                  f"⚡⚡Yoqilg'i turi:              <b>{specifications["engine_type"]}</b>\n"
                                  f"🐎⚡Ot kuchi:                   <b>{specifications["horsepower"]}</b>\n"
                                  f"⚙️🔀Transmissiya:               <b>{specifications["transmission"]}</b>\n"
                                  f"📏➡️Uzunligi:                   <b>{specifications["length"]} mm</b>\n"
                                  f"📏⬆️Balandligi:                 <b>{specifications["height"]} mm</b>\n"
                                  f"📏↔️Eni:                        <b>{specifications["width"]} mm</b>\n"
                                  f"⚫📏Diska diametri:             <b>{specifications["disk_diameter"]} dyum</b>\n"
                                  f"📦🚗Bagaj sig'imi:              <b>{specifications["cargo_capacity"]} litr</b>\n"
                                  f"🪑🚘O'rindiqlar soni:           <b>{specifications["seat_capacity"]}</b>\n"
                                  f"🔋🧪Batareya turi:              <b>{specifications["battery_type"]}</b>\n"
                                  f"📍🚗💨Probeg:                   <b>{specifications["probeg"]}</b>\n"
                                  f"🛡️📜Garantiya:                  <b>{specifications["guarantee"]}</b>\n"
                                  f"🎨🚗Rangi:                      <b>{specifications["color"]}</b>\n"
                                  f"</pre>", parse_mode="HTML")
        await call.message.answer("\n".join(comforts_list))

