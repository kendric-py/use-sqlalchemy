from aiogram.types import Message
from aiogram import Router

from sqlalchemy.ext.asyncio import AsyncSession

from database import requests as db

router = Router()


@router.message(commands='start')
async def start_cmd(message: Message, session: AsyncSession):
    await db.new_user(session, message.chat.id, message.from_user.first_name)
    await message.answer('Добро пожаловать')