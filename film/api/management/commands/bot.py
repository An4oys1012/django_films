from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from configure import cfg

storage = MemoryStorage()
bot = Bot(token=cfg['token'])
dp = Dispatcher(bot, storage=storage)
