import asyncio
from datetime import date

import sqlalchemy.exc
from sqlalchemy import select, delete

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark

from logger import logger


async def delete_student(st_id: int):
    async with async_session as session:
        try:
            stmt = (delete(Student)
                    .where(Student.id == st_id)
                    .execution_options(synchronize_session="fetch"))
            await session.execute(stmt)
            await session.commit()
            logger.debug(f'student - {st_id} - was deleted')
        except sqlalchemy.exc.IntegrityError as err:
            logger.debug(f'Error - {err}')

