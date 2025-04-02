import asyncio

from aiogram import Router, F, types
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                                 CallbackQuery, FSInputFile)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import datetime
from dotenv import load_dotenv
import pickle
import os

from create_bot import bot
from utils import get_Car_Spicifications, Output_Car_Specifications, get_Car_models

from keyboards.Keys import (main_keyboard, cars_keyboard, filial_keyboard, request_keyboard, get_light_car_brands_inline, get_light_car_models_inline,
                            get_truck_brands_inline, get_truck_models_inline, get_car_options_inline)

load_dotenv()
start_router = Router()

view_stats = get_Car_models.Get_Car_models()
req_stats = get_Car_models.Get_Car_models()

user_counter = set()
brand = ""
model = ""
last_model = ""
comforts_list = []
my_dic = {}

saved_models = []

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

BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")

# Handler for "Cars" button
@start_router.message(lambda message: message.text == "🚗Avtomobillar")
async def cars_handler(message: types.Message):
    text = "Avtomobil turini tanlang: "
    await message.answer(text, reply_markup=cars_keyboard)

@start_router.message(lambda message: message.text == "🚗Yengil avtomobillar")
async def yengil_avto_handler(message: types.Message):
    text = "🚗Avtomobil brandini tanlang:"
    await message.answer(text, reply_markup=get_light_car_brands_inline())

# =========================== Truck Cars =================================================
@start_router.message(lambda message: message.text == "🚚Yuk avtomobillar")
async def yuk_avto_handler(message: types.Message):
    text = "🚚Yuk avtomobillar:"
    await message.answer(text, reply_markup=get_truck_brands_inline())

@start_router.callback_query(F.data.startswith("Brand_"))
async def car_brand_handler(call: CallbackQuery):
    brand = call.data.split("_")[1]  # Extract brand name
    await call.message.answer(f"🚘 {brand} models:", reply_markup=get_truck_models_inline(brand))

# Handling inline button presses for car models
@start_router.callback_query(F.data.startswith("Model_"))
async def car_model_handler(call: CallbackQuery, state: FSMContext):
    global model
    model = call.data.split("_")[1]  # Extract model name
    await state.update_data(car_model=model)
    await call.message.answer(f"🚘 {model} xarakteristikasi...\n\nIltmos tanlang:",
                              reply_markup=get_car_options_inline())


# Handler for "Back" button inside car models (returns to brands)
@start_router.callback_query(F.data == "Back_to_brands")
async def back_to_brands(call: CallbackQuery):
    await call.message.answer("🚗 Avtomobil brendini tanlang:", reply_markup=get_truck_brands_inline())
# ========================================================================================

# Handler to go back to the main menu
@start_router.message(lambda message: message.text == "🔙 Orqaga")
async def back_to_main_menu(message: types.Message):
    text = "🏠 Bosh menu:"
    await message.answer(text, reply_markup=main_keyboard)
#======================================================================================

# Handling inline button presses for car brands (show models)
@start_router.callback_query(F.data.startswith("brand_"))
async def car_brand_handler(call: CallbackQuery):
    global brand
    brand = call.data.split("_")[1]  # Extract brand name
    await call.message.answer(f"🚘 {brand} models:", reply_markup=get_light_car_models_inline(brand))

# Handling inline button presses for car models
@start_router.callback_query(F.data.startswith("model_"))
async def car_model_handler(call: CallbackQuery, state: FSMContext):
    global model
    model = call.data.split("_")[1]  # Extract model name
    await state.update_data(car_model=model)
    await call.message.answer(f"🚘{brand} {model}\n\nIltmos tanlang:", reply_markup=get_car_options_inline())

# Handler for "Back" button inside car models (returns to brands)
@start_router.callback_query(F.data == "back_to_brands")
async def back_to_brands(call: CallbackQuery):
    await call.message.answer("🚗 Avtomobil brendini tanlang:", reply_markup=get_light_car_brands_inline())


# Handler for "Back" button inside inline car list
@start_router.callback_query(F.data == "back_to_cars")
async def back_to_cars(call: CallbackQuery):
    await call.message.answer("🚗 Avtomobil turini tanlang:", reply_markup=cars_keyboard)

# Handler for "Leave the request" button (asks for user's name)
@start_router.callback_query(F.data == "leave_request")
async def leave_request_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("📝 Ismingini kiriting:")
    await state.set_state(RequestState.waiting_for_name)

# Handler for user sending their name
@start_router.message(RequestState.waiting_for_name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📞 Telefon no'meringizni kiriting.",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[[KeyboardButton(text="📲 Telefon no'mer", request_contact=True)]],
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
    await message.answer("✅ Sizning so'rovingiz qabul qilindi!", reply_markup=main_keyboard)
    from aiogram_run import redis_client

    user_id = message.from_user.id
    user_key = f"user:{user_id}:requests"

    if not redis_client.sismember(user_key, model):
        req_stats[f"{model}"] += 1

    redis_client.sadd(user_key, model)
    dic = pickle.dumps(req_stats)
    redis_client.set('req_stats', dic)

    car_models = redis_client.smembers(user_key)
    for car in car_models:
        print(car.decode())

    # ss = redis_client.get('req_stats')
    # global my_dic
    # my_dic = pickle.loads(ss)
    # print(my_dic)

    await state.clear()


@start_router.callback_query(F.data == "contact_manager")
async def contact_manager_handler(call: CallbackQuery):
    manager_info = "👨‍💼 Manager Contact:\n📞 +998909528282\n📩 Telegram: @temurbek_tashkent_motors"
    await call.message.answer(manager_info)

# Car specifications
@start_router.callback_query(F.data == "car specifications")
async def car_specifications(call: CallbackQuery, state: FSMContext):
    from aiogram_run import redis_client

    user_id = call.from_user.id
    user_key = f"user:{user_id}:views"

    if not redis_client.sismember(user_key, model):
        view_stats[f"{model}"] += 1

    redis_client.sadd(user_key, model)
    dic = pickle.dumps(view_stats)
    redis_client.set('view_stats', dic)

    car_models = redis_client.smembers(user_key)
    for car in car_models:
        print(car.decode())


    photos = get_Car_Spicifications.get_car_photo_by_model_filtered(model)
    # ------------------------------Rasmlarni jo'natish-----------------------------------#
    if not photos:
        await call.message.answer("Bu avtomobil uchun rasmlar yo'q")
        return
    media_group = []

    # await call.message.answer("Iltmos kuting...")
    # await asyncio.sleep(3)
    for photo in photos:
        file = FSInputFile(photo.photo_url)
        media_group.append(types.InputMediaPhoto(media=file))
    if len(media_group) == 1:
        await bot.send_photo(user_id, media_group[0].media)
    else:
        await bot.send_media_group(user_id, media_group)
    # ----------------------------------------------------------------------------------------
    await call.message.answer(f"<pre>{Output_Car_Specifications.getCarSpecifications(model)}</pre>", parse_mode="HTML", reply_markup=get_car_options_inline())
    # ss = redis_client.get('view_stats')
    # global my_dic
    # my_dic = pickle.loads(ss)



