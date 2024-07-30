import asyncio

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from sqlalchemy import delete


async def delete_groups():
    async with async_session as session:
        stmt = delete(Group)
        await session.execute(stmt)
        await session.commit()
        return True


async def delete_students():
    async with async_session as session:
        stmt = delete(Student)
        await session.execute(stmt)
        await session.commit()
        return True


async def delete_teachers():
    async with async_session as session:
        stmt = delete(Teacher)
        await session.execute(stmt)
        await session.commit()
        return True


async def delete_subjects():
    async with async_session as session:
        stmt = delete(Subject)
        await session.execute(stmt)
        await session.commit()
        return True


async def delete_marks():
    async with async_session as session:
        stmt = delete(Mark)
        await session.execute(stmt)
        await session.commit()
        return True


async def delete_tables():
    await delete_groups()
    await delete_students()
    await delete_teachers()
    await delete_subjects()
    await delete_marks()


if __name__ == '__main__':
    asyncio.run(delete_tables())
