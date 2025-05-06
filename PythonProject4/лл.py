import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7688570789:AAGpfAHGQ10mwuxc5JYEDiVveTSoP3Y9J5w"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def send_webapp_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть WebApp",
            web_app=WebAppInfo(url="#")
        )]
    ])
    await message.answer("Нажми кнопку ниже для открытия WebApp:", reply_markup=keyboard)

async def main():
    dp.include_router(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
