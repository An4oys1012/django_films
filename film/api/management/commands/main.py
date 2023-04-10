from aiogram.utils import executor

from bot import dp
from handlers import client

client.register_client()

executor.start_polling(dp, skip_updates=True)
