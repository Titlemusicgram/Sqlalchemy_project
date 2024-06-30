import asyncio

from config import settings
from sqlalchemy import URL, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine(url=settings.db_url_asyncpg, echo=True)


async def get_something():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3"))
        print(f"{res.all()=}")


asyncio.run(get_something())
