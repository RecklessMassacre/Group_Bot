from random import randint, choice
from aiogram import types, Dispatcher


SAD_EMOJI = ['😒', '☹️', '😣', '🥺', '😞', '🙄', '😟', '😠', '😕', '😖', '😫', '😩', '😰', '😭']
HAPPY_EMOJI = ['😀', '😏', '😱', '😂', '😁', '😂', '😉', '😊', '😋', '😎', '☺', '😏']
GIRL_EMOJI = ['🥰', '😍', '🤭', '😻', '😍', '👉👈']


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
#     await message.reply(message.text)  # answers using tg reply system
#     await bot.send_message(message.from_user.id, message.text)  # privately reply


# @dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    txt = "/size, /s - Daily cock size"
    await message.answer(txt)


# @dp.message_handler(commands=['size', 's'])
async def cock_size(message: types.Message):
    size = get_cock_size()
    if size < 0:
        await message.answer(f"your size is {size} см. Позравляю, вы сегодня девотька {choice(GIRL_EMOJI)}")
    elif size > 15:
        await message.answer(f"your size is {size} см. Да вы половой гигант сегодня {choice(HAPPY_EMOJI)}")
    elif size < 10:
        await message.answer(
            f"your size is {size} см. {choice(SAD_EMOJI)} Возможно, ваша половая зрелость еще впереди...")
    else:
        await message.answer(f"your size is {size} см. В пределах нормы 😐")


def get_cock_size():
    possible_sizes = [randint(-16, -7), randint(4, 25), randint(4, 25), randint(4, 25), randint(4, 25)]
    size = choice(possible_sizes)

    return size


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(cock_size, commands=['size', 's'])
