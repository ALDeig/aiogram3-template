from sqlalchemy.ext.asyncio import AsyncSession

from app.src.services.db.dao.user_dao import UserDao


async def save_user(
    session: AsyncSession, user_id: int, full_name: str, username: str | None
):
    await UserDao(session).insert_or_nothing(
        index_element="id", id=user_id, full_name=full_name, username=username
    )
