import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6303762984:AAGyioGY4N-hK7S6dDBYEFfME93lwRtTH6k")
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ существую для того, чтобы ты смотрел(а) на фоточки сырков!")

@dp.message(Command("album"))
async def cmd_album(message: Message):
    album_builder = MediaGroupBuilder(
        caption="вот ваши сырочки."
    )
    album_builder.add_photo(
        media="https://svitlogorie.ru/wp-content/uploads/2023/11/Fonovaya-kartinka-1.png"
    )
    album_builder.add_photo(
        media="https://media.vprok.ru/products/x700/sc/tq/hev2lbpjpqyg72w2m5swf74nohx7tqsc.jpeg"
    )
    album_builder.add_photo(
        media="https://main-cdn.sbermegamarket.ru/big2/hlr-system/-92/208/399/541/719/14/100032766088b0.jpg"
    )
    album_builder.add_photo(
        media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS5byJy126Iaf49xYlJyxxiEd3pDv0qKtx8Q&s"
    )

    await message.answer_media_group(
        media=album_builder.build()
    )
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())