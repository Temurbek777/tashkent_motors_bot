from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,
                            InlineKeyboardMarkup)
from utils import get_Cars, get_Car_Spicifications


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍💼Menejer")],
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
            [InlineKeyboardButton(text="📩 So'rov qoldirish", callback_data="leave_request")],
            [InlineKeyboardButton(text="👨‍💼 Menejer bilan bog'lanish", callback_data="contact_manager")]
        ]
    )