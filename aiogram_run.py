import asyncio
from create_bot import bot, dp
from handlers.manager_handler import manager_router
from handlers.start import start_router
from handlers.menu_handlers import set_bot_menu
import redis

# from work_time.time_func import send_time_msg

redis_client = redis.Redis(host='localhost', port=6379, db=0)

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()

    redis_client.flushdb()
    print("Redis database cleared!")
    await set_bot_menu()
    dp.include_router(start_router)
    dp.include_router(manager_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())