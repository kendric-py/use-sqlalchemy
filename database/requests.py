from sqlalchemy.ext.asyncio import AsyncSession
from .models import User


async def new_user(session: AsyncSession, user_id: int, name: str) -> User:
    user = User(id=user_id, name=name)
    session.add(user)
    await session.commit()
    return(session)