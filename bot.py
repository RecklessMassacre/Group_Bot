from aiogram.utils import executor
from create_bot import dp


# connection to db here
async def on_startup(_):
    print("bot is running")


async def on_shutdown(_):
    print("bot has been shutdown")


def main():
    from handlers import client
    client.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == "__main__":
    main()
