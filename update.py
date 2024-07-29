import asyncio
from datetime import date

import sqlalchemy.exc

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from sqlalchemy import update, select

from logger import logger


async def update_student(st_id: int, fullname: str, group_number: str):
    name = fullname.split(' ')[-2:][0]
    async with async_session as session:
        async with session.begin():
            try:
                stmt = select(Group.id).where(Group.number == group_number)
                result = await session.execute(stmt)
                group_id = result.scalar()

                stmt = (update(Student)
                        .where(Student.id == st_id)
                        .values(name=name, fullname=fullname, group_id=group_id)
                        .execution_options(synchronize_session="fetch"))
                await session.execute(stmt)
                await session.commit()
                logger.debug(f'student - {fullname} - was updated')
            except sqlalchemy.exc.IntegrityError as err:
                logger.debug(f'Error - {err}')