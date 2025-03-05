from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                BotCommand, MenuButtonCommands,
                InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import datetime

from create_bot import bot
from utils import get_Cars

start_router = Router()

GROUP_CHAT_ID = -1002495308094

# Define states for user input
class RequestState(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()

# Car shop details
SHOP_NAME = "Tashkent Motors"
SHOP_ADDRESS = "Tashkent halqa yo'li, O'zgarish ko'chasi"
WORKING_HOURS = "8:30-18:00 Du-Shan"
SHOP_LATITUDE = 41.2440635  # Replace with actual latitude
SHOP_LONGITUDE = 69.2279954  # Replace with actual longitude
#===========================================================

# Manager details
NAME = "Rajabov Temurbek"
PHONE_NUMBER = "+998909528282"
TG_USERNAME = "@temurbek_tashkent_motors"

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menejer bilan bog'lanish")],
        [KeyboardButton(text="Avtomobillar")],
        [KeyboardButton(text="Extiyot qismlar")]
    ],
    resize_keyboard=True
)

# Submenu keyboard for "Cars"
cars_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yengil avtomobillar")],
        [KeyboardButton(text="Yuk avtomobillar")],
        [KeyboardButton(text="🔙 Orqaga")]  # Button to go back to the main menu
    ],
    resize_keyboard=True
)

# Car brands and their models
# car_brands = {
#     "Toyota": ["Camry", "Corolla", "Land Cruiser"],
#     "BMW": ["X5", "M3", "i8"],
#     "Mercedes": ["E-Class", "C-Class", "GLS"]
# }

car_brands = get_Cars.get_all_car_brands()

# Inline buttons for car brands
def get_car_brands_inline():
    keyboard = [
        [InlineKeyboardButton(text=f"🚗 {brand}", callback_data=f"brand_{brand}")]
        for brand in car_brands
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_to_cars")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Inline buttons for car models
def get_car_models_inline(brand):
    models = car_brands.get(brand, [])
    keyboard = [
        [InlineKeyboardButton(text=f"🚘 {model}", callback_data=f"model_{model}")]
        for model in models
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_to_brands")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Inline buttons after selecting a car model
def get_car_options_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚗Mashina Xarakteristikasini ko'rish", callback_data="car specifications")],
            [InlineKeyboardButton(text="📩 Leave the request", callback_data="leave_request")],
            [InlineKeyboardButton(text="👨‍💼 Manager", callback_data="contact_manager")]
        ]
    )


async def set_bot_menu():
    commands = [
        BotCommand(command="start", description="Start"),
        BotCommand(command="info", description="Salon haqida malumot olish"),
        BotCommand(command="sotuv_manejeri", description="Sotuv menejeri bilan bog'lanish"),
        BotCommand(command="filiallar", description="Salonimiz fialiallari")
    ]
    await bot.set_my_commands(commands)  # Set the commands in the menu
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())  # Set the menu button


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    text = "👋 Tashkent Motors Botga xush kelibsiz!\nIltmos pastdagi so'rovlarni tanlang:"

    await message.answer(text, reply_markup=main_keyboard)

# Handler for "Cars" button
@start_router.message(lambda message: message.text == "Avtomobillar")
async def cars_handler(message: types.Message):
    text = "🚗 Avtomobil brandini tanlang:"
    await message.answer(text, reply_markup=get_car_brands_inline())

# Handler to go back to the main menu
@start_router.message(lambda message: message.text == "🔙 Orqaga")
async def back_to_main_menu(message: types.Message):
    text = "🏠 Main menu:"
    await message.answer(text, reply_markup=main_keyboard)


# Handling inline button presses for car brands (show models)
@start_router.callback_query(F.data.startswith("brand_"))
async def car_brand_handler(call: CallbackQuery):
    brand = call.data.split("_")[1]  # Extract brand name
    await call.message.answer(f"🚘 {brand} models:", reply_markup=get_car_models_inline(brand))

# Handling inline button presses for car models
@start_router.callback_query(F.data.startswith("model_"))
async def car_model_handler(call: CallbackQuery, state: FSMContext):
    model = call.data.split("_")[1]  # Extract model name
    await state.update_data(car_model=model)
    await call.message.answer(f"🚘 {model} details...\n\nPlease choose an option:", reply_markup=get_car_options_inline())

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
    await call.message.answer(f"Brand🔰: {specifications["brand"]}\n"
                              f"Model🚘: {specifications["model"]}\n"
                              f"Yil📆: {specifications["year"]}\n"
                              f"Narxi: {specifications["price"]}\n"
                              f"Holati: {specifications["condition"]}\n"
                              f"Kuzov turi: {specifications["body_type"]}\n"
                              f"Yoqilg'i turi: {specifications["engine_type"]}\n"
                              f"Dvigatel hajmi: {specifications["engine_size"]}\n"
                              f"Ot kuchi: {specifications["horsepower"]}\n"
                              f"Transmissiya: {specifications["transmission"]}\n"
                              f"Yoqilg'i sarfi: {specifications["fuel_spending"]}\n"
                              f"Uzunligi: {specifications["length"]}\n"
                              f"Balandligi: {specifications["height"]}\n"
                              f"Eni: {specifications["width"]}\n"
                              f"Diska diametri: {specifications["disk_diameter"]}\n"
                              f"Bagaj sig'imi: {specifications["cargo_capacity"]}\n"
                              f"O'rindiqlar soni: {specifications["seat_capacity"]}\n"
                              # f"Probeg: {specifications["probeg"]}"
                              f"Garantiya: {specifications["guarantee"]}\n"
                              f"Rangi: {specifications["color"]}\n")


# ------------------ Avtosalon haqida ma'lumot -------------------------
@start_router.message(Command("info"))
async def show_menu(message: Message):
    text = (
        f"🏪 *{SHOP_NAME}*\n"
        f"📍 Address: {SHOP_ADDRESS}\n"
        f"🕒 Ish vaqti:\n{WORKING_HOURS}\n"
        f"📞 Contact: +998909528282\n"
        f"🌍 Website: [Visit Us](https://example.com)"
    )

    await message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)

    # Send location
    await bot.send_location(chat_id=message.chat.id, latitude=SHOP_LATITUDE, longitude=SHOP_LONGITUDE)
# =======================================================================

#-----------------------Sotuv menejeri bilan bog'lanish ----------------------------
@start_router.message(Command("sotuv_manejeri"))
async def help_handler(message: Message):
    text = (
        f"🕒 FIO:\n{NAME}\n"
        f"📞 Contact: {PHONE_NUMBER}\n"
        f"🌍 Telegram: [{TG_USERNAME}](https://t.me/{TG_USERNAME[1:]})"
    )
    await message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)
# =======================================================================================

@start_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Need help? Contact support.")
