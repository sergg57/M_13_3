# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "8097951435:AAEZRi934nIqcJ-udhBVZP_YZM3tylO5rdk"
bot = Bot(api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью!")

@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer(f'Введите команду /start, чтобы начать общение!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)