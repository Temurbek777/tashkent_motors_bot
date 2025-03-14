from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from .start import start_router
from .start import SHOP_NAME,SHOP_ADDRESS,SHOP_LONGITUDE,SHOP_LATITUDE,WORKING_HOURS,NAME,TG_USERNAME,PHONE_NUMBER
from keyboards.Keys import main_keyboard

manager_router = Router()

#-----------------------Sotuv menejeri bilan bog'lanish ----------------------------
@manager_router.message(lambda message: message.text == "👨‍💼Menejer")
async def help_handler(message: types.Message):
    print(f"Received message: {message.text}")  # Debug log
    text = (
        f"🕒 FIO:\n{NAME}\n"
        f"📞 Contact: {PHONE_NUMBER}\n"
        f"🌍 Telegram: [{TG_USERNAME}](https://t.me/{TG_USERNAME[1:]})"
    )
    await message.answer(text, reply_markup=main_keyboard)
# =======================================================================================