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


async def delete_teacher(tr_id: int):
    async with async_session as session:
        try:
            stmt = (delete(Teacher)
                    .where(Teacher.id == tr_id)
                    .execution_options(synchronize_session="fetch"))
            await session.execute(stmt)
            await session.commit()
            logger.debug(f'teacher - {tr_id} - was deleted')
        except sqlalchemy.exc.IntegrityError as err:
            logger.debug(f'Error - {err}')


async def delete_group(gr_id: int):
    async with async_session as session:
        stmt = (delete(Group)
                .where(Group.id == gr_id)
                .execution_options(synchronize_session="fetch"))
        await session.execute(stmt)
        await session.commit()
        logger.debug(f'group - {gr_id} - was deleted')
        return True


async def delete_subject(sub_id: int):
    async with async_session as session:
        stmt = (delete(Subject)
                .where(Subject.id == sub_id)
                .execution_options(synchronize_session="fetch"))
        await session.execute(stmt)
        await session.commit()
        logger.debug(f'group - {sub_id} - was deleted')
        return True
