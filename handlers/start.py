from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, MenuButtonCommands
from create_bot import bot

start_router = Router()

# Creating a reply keyboard
# reply_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Option 1"), KeyboardButton(text="Option 2")],
#         [KeyboardButton(text="Exit")]
#     ],
#     resize_keyboard=True
# )

async def set_bot_menu():
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="info", description="Get bot information"),
        BotCommand(command="help", description="Help and support"),
    ]
    await bot.set_my_commands(commands)  # Set the commands in the menu
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())  # Set the menu button


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

@start_router.message(Command("menu"))
async def show_menu(message: Message):
    """Send the reply keyboard menu."""
    await message.answer("Choose an option:", reply_markup=reply_keyboard)

@start_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Need help? Contact support.")