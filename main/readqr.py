from createbot import dp,bot
from aiogram import types,Dispatcher
import cv2
from aiogram.types import ContentType
import numpy as np
from main import readqr,votesdata
from .keyboard import kb 
from.keyboard import get_value
from .votesdata import get_result



async def hello_send(message:types.Message):
    await message.answer(f'Привіт {message.from_user.full_name}! Це бот створений для голосування серед учнів та персоналу ліцею на пост мера нашого ліцею.Прошу тебе скинути в чат боту фото своєї перепустки (QRкод) щоб ми могли переконатись що ти голосуєш вперше.Бот буде ігнорувати будь який текст чи фото без твого QR коду ')


async def read_qr(message:types.Message):
    global value

    try:
        photo = message.photo[-1]  
        photo_id = photo.file_id
        file_info = await bot.get_file(photo_id)

        photo_content = await bot.download_file(file_info.file_path)

        nparr = np.frombuffer(photo_content.getvalue(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img_np)
        
        if votesdata.vote_check(value):    
            await message.answer(f'ok, go choose your candidat',reply_markup=kb) 
            
        else:
            await message.answer('you already vote')

            
        
        get_value(value)
        
        
    except Exception as e:
        print(f'ay{e} problem blin')


async def result(message:types.Message):
    lst_v = get_result()
    text =''
    chk=0
    for i in lst_v:
        if chk == 0:
            txt = f'Богдан Нестерчук:{i}\n'
            text+=txt
            chk+=1
            continue
        
        if chk == 1:
            txt = f'Бордаков Дмитро:{i}\n'
            text+=txt
            chk+=1
            continue

        if chk == 2:
            txt = f'Саша Булачок:{i}\n'
            text+=txt
            chk+=1
            continue

        if chk == 3:
            txt = f'Борислава:{i}\n'
            text+=txt
            chk+=1
            continue

        if chk == 4:
            txt = f'Богдан Чернюк:{i}\n'
            text+=txt
            chk+=1
            continue

        if chk == 5:
            break
    await message.answer(text)
        
    

def register_handlers_readqr(dp: Dispatcher):
    dp.register_message_handler(hello_send,commands=['start'])
    dp.register_message_handler(read_qr, content_types=ContentType.PHOTO)
    dp.register_message_handler(result,commands=['result']  )