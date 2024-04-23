from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types,Dispatcher
from createbot  import dp,bot 
from main import readqr,votesdata
from .votesdata import add_vote, block_vote
# from .readqr import value


def get_value(val):
    global num
    num =val



kb = InlineKeyboardMarkup(row_width=3)

butt1 = InlineKeyboardButton(text='Bohdan Nesterchuk',callback_data='bro')
butt2 = InlineKeyboardButton(text='Dima Bordakov',callback_data='dima')
butt3 = InlineKeyboardButton(text='Sasha Bulachok',callback_data='sasha')
butt4 = InlineKeyboardButton(text='Bohdan Chernyuk',callback_data='chrnk')
butt5 = InlineKeyboardButton(text='Borislava',callback_data='brslv')


kb.add(butt1)
kb.add(butt2)
kb.add(butt3)
kb.add(butt4)
kb.add(butt5)

async def if_i(callback:types.CallbackQuery):
    if votesdata.vote_check(num):    
        await callback.message.answer(num)
        await callback.answer('Bro❤️')
        add_vote(w=1)
        block_vote(num)
        
    else:
        await callback.message.answer('you already vote')



async def if_dima(callback:types.CallbackQuery):
    if votesdata.vote_check(num):   
        await callback.message.answer('Bordakov')
        add_vote(w=2)
        block_vote(num)
        
    else:
        await callback.message.answer('you already vote')


async def if_Sasha(callback:types.CallbackQuery):
    if votesdata.vote_check(num):   
        await callback.message.answer('Sasha')
        add_vote(w=3)
        block_vote(num)
        
    else:
        await callback.message.answer('you already vote')


async def if_borislava(callback:types.CallbackQuery):
    if votesdata.vote_check(num):   
        await callback.message.answer('Borislava')
        add_vote(w=4)
        block_vote(num)
        
    else:
        await callback.message.answer('you already vote')

    
async def if_chernyuk(callback:types.CallbackQuery):
    if votesdata.vote_check(num):   
        await callback.message.answer('Chernyuk')
        add_vote(w=5)
        block_vote(num)
        
    else:
        await callback.message.answer('you already vote')


def register_handlers_langkb(dp:Dispatcher):
    dp.register_callback_query_handler(if_i,text='bro')
    dp.register_callback_query_handler(if_dima,text='dima')
    dp.register_callback_query_handler(if_Sasha,text='sasha')
    dp.register_callback_query_handler(if_borislava,text='brslv')
    dp.register_callback_query_handler(if_chernyuk,text='chrnk')
    