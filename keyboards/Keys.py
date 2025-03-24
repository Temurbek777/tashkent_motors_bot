from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,
                            InlineKeyboardMarkup)
from utils import get_Cars, get_Car_Spicifications


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍💼Menejer bilan bog'lanish")],
        [KeyboardButton(text="🚗Avtomobillar")],
        [KeyboardButton(text="⚙️Extiyot qismlar")]
    ],
    resize_keyboard=True
)

# Submenu keyboard for "Cars"
cars_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚗Yengil avtomobillar")],
        [KeyboardButton(text="🚚Yuk avtomobillar")],
        [KeyboardButton(text="🔙 Orqaga")]  # Button to go back to the main menu
    ],
    resize_keyboard=True
)

filial_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"🏪Tashkent filiali"), KeyboardButton(text="🏪Buxoro filiali")],
        [KeyboardButton(text=f"🏪Xorazm filiali"), KeyboardButton(text="🏪Nukus filiali")],
        [KeyboardButton(text=f"🏪Termiz filiali"), KeyboardButton(text="🏪Navoiy filiali")],
        [KeyboardButton(text=f"🏪Qarshi filiali")]
    ],
    resize_keyboard=True
)

request_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"📩So'rov qoldirish")],
        [KeyboardButton(text=f"👨‍💼Menejer bilan bog'lanish")]
    ],
    resize_keyboard=True
)

light_car_brands = get_Cars.get_all_light_car_brands()
truck_car_brands = get_Cars.get_all_truck_brands()

# ===========================Inline buttons for light car brands ===============================
def get_light_car_brands_inline():
    keyboard = [
        [InlineKeyboardButton(text=f"🚗 {brand}", callback_data=f"brand_{brand}")]
        for brand in light_car_brands
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_to_cars")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Inline buttons for car models
def get_light_car_models_inline(brand):
    models = light_car_brands.get(brand, [])
    keyboard = [
        [InlineKeyboardButton(text=f"🚘 {model}", callback_data=f"model_{model}")]
        for model in models
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_to_brands")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
# ================================================================================================

# ===============================Inline buttons for trucks========================================
def get_truck_brands_inline():
    keyboard = [
        [InlineKeyboardButton(text=f"🚗 {brand}", callback_data=f"Brand_{brand}")]
        for brand in truck_car_brands
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="back_to_cars")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Inline buttons for car models
def get_truck_models_inline(brand):
    models = truck_car_brands.get(brand, [])
    keyboard = [
        [InlineKeyboardButton(text=f"🚘 {model}", callback_data=f"Model_{model}")]
        for model in models
    ]
    keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="Back_to_brands")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
# =================================================================================================

# Inline buttons after selecting a car model
def get_car_options_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚗Mashina Xarakteristikasini ko'rish", callback_data="car specifications")],
            [InlineKeyboardButton(text="📩 So'rov qoldirish", callback_data="leave_request")],
            [InlineKeyboardButton(text="👨‍💼 Menejer bilan bog'lanish", callback_data="contact_manager")]
        ]
    )

