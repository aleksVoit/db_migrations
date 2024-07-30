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


async def update_teacher(tr_id: int, fullname: str):
    name = fullname.split(' ')[-2:][0]
    async with async_session as session:
        async with session.begin():
            try:
                stmt = (update(Teacher)
                        .where(Teacher.id == tr_id)
                        .values(name=name, fullname=fullname)
                        .execution_options(synchronize_session="fetch"))
                await session.execute(stmt)
                await session.commit()
                logger.debug(f'student - {fullname} - was updated')
            except sqlalchemy.exc.IntegrityError as err:
                logger.debug(f'Error - {err}')


async def update_subject(sub_id: int, sub_name: str, sub_teacher: str):
    async with async_session as session:
        async with session.begin():
            stmt = (select(Teacher.id)
                    .where(Teacher.fullname == sub_teacher))
            result = await session.execute(stmt)
            teacher_id = result.fetchone()[0]
            stmt = (update(Subject)
                    .where(Subject.id == sub_id)
                    .values(name=sub_name, teacher_id=teacher_id)
                    .execution_options(synchronize_session="fetch"))
            await session.execute(stmt)
            await session.commit()
            logger.debug(f'subject - {sub_id} - was updated')
            return True


async def update_group(gr_id: int, gr_number: str):
    async with async_session as session:
        async with session.begin():
            stmt = (update(Group)
                    .where(Group.id == gr_id)
                    .values(number=gr_number)
                    .execution_options(synchronize_session="fetch"))
            await session.execute(stmt)
            await session.commit()
            logger.debug(f'Group - {gr_id} - was updated')
            return True
