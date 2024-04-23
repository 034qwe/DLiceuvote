from aiogram.utils import executor
from createbot import dp
from main import readqr,votesdata,keyboard


async def on_startup(_):
    print('bot start')
    votesdata.data_start()



readqr.register_handlers_readqr(dp)
keyboard.register_handlers_langkb(dp)

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)