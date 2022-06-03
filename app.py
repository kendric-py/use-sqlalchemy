from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import asyncio

from telegram.DBSessionMiddleware import DBSessionMiddleware
from telegram.handlers import router
from database.base import Base


connection_url = 'sqlite+aiosqlite:///data/database.db'


async def _create_db_pool(connect_url: str):
    engine = create_async_engine(connect_url, future=True, echo=False)
    pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    return(pool)



async def main():
    db_pool = await _create_db_pool(connection_url)
    bot = Bot(token='1712226565:AAHOPiqALuKWtuGgpY1jwWGDyygcrIyqMHI')
    dp = Dispatcher()
    dp.message.middleware(DBSessionMiddleware())
    dp.include_router(router)
    await dp.start_polling(bot, db_pool=db_pool)
    

if __name__ == '__main__':
    asyncio.run(main())