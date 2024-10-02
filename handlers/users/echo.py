from aiogram import types, F
from utils.downloader import Mp3Downloader
from youtubesearchpython import VideosSearch
import glob
import os

from keyboards.default import button

from loader import dp, bot

def words_to_numbers(word: str):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9
    elif word == "ten":
        return 10

@dp.message(F.content_type==types.ContentType.TEXT)
async def echo(message: types.Message):
    global videos_url
    await message.answer("Qo'shiq qidirilmoqda")
    search = VideosSearch(message.text, limit=10)
    videos_url = [url['link'] for url in search.result()['result']]
    data = ""
    for i, title in enumerate(search.result()['result']):
        data += f"{i+1} {title['title']}\n"
    await message.answer(data, reply_markup=button)

@dp.callback_query()
async def call(call: types.CallbackQuery):
    number = words_to_numbers(str(call.data))
    Mp3Downloader(videos_url[number - 1])
    try:
        await call.message.answer_audio(types.FSInputFile(glob.glob("*.mp3")[0]))
    except Exception as e:
        print(e)
    try:
        os.remove(glob.glob("*.mp3")[0])
    except:
        pass