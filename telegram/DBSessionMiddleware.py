from aiogram import BaseMiddleware


class DBSessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        db_pool = data['db_pool']
        async with db_pool() as session:
            data['session'] = session
            return(await handler(event, data))