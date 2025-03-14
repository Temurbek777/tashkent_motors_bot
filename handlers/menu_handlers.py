from aiogram.types import (Message, BotCommand, MenuButtonCommands)
from aiogram.filters import CommandStart, Command
from aiogram import Router
from handlers.start import start_router
from keyboards.Keys import main_keyboard, filial_keyboard
from create_bot import bot
from .start import start_router
from .start import SHOP_NAME,SHOP_ADDRESS,SHOP_LONGITUDE,SHOP_LATITUDE,WORKING_HOURS,NAME,TG_USERNAME,PHONE_NUMBER


async def set_bot_menu():
    commands = [
        BotCommand(command="start", description="Start"),
        BotCommand(command="info", description="Salon haqida malumot olish"),
        BotCommand(command="sotuv_manejeri", description="Sotuv menejeri bilan bog'lanish"),
        BotCommand(command="filiallar", description="Salonimiz fialiallari")
    ]
    await bot.set_my_commands(commands)  # Set the commands in the menu
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())  # Set the menu button

# -------------------------Start Command--------------------------------
@start_router.message(Command("start"))
async def cmd_start(message: Message):
    text = "👋 Tashkent Motors Botga xush kelibsiz!\nIltmos pastdagi so'rovlarni tanlang:"

    await message.answer(text, reply_markup=main_keyboard)
# ===========================================================================

# ------------------ Avtosalon haqida ma'lumot -------------------------
@start_router.message(Command("info"))
async def show_menu(message: Message):
    text = (
        f"🏪 *{SHOP_NAME}*\n"
        f"📍 Address: {SHOP_ADDRESS}\n"
        f"🕒 Ish vaqti:\n{WORKING_HOURS}\n"
        f"📞 Contact: +998909528282\n"
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

#--------------------------------- Filiallar ----------------------------------
@start_router.message(Command("filiallar"))
async def help_handler(message: Message):
    await message.answer("Filialni tanlang:", reply_markup=filial_keyboard)
#==============================================================================