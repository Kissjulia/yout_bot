from pytube import YouTube
from config import dp, bot
from aiogram import types
from aiogram import Bot, Dispather
from aiogram.dispatcher.filters import Text

@dp.message_handler(commands='start')
async def start_bot(message: types.Message, inline_keyboard=None):
    print(message.text)
    await message.answer('Привет! Введи адрес: ')

@dp.message_handler(commands='url')
async def input_URL(message: types.Message):
    msg = message.text.split()
    if len(msg) > 2:
        res = msg[2]
    else:
        res = '720p'
    yt = YouTube(msg[1])
    print(yt.watch_url)
    path = yt.title
    yt.streams.filter(resolution=res).first().download('')



