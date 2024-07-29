import asyncio
from datetime import date

import sqlalchemy.exc
from sqlalchemy import select

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark

from logger import logger


async def read_student(st_id: int):
    async with async_session as session:
        stmt = (select(Student.id, Student.fullname, Student.group_id)
                .select_from(Student)
                .where(Student.id == st_id))
        result = await session.execute(stmt)
        student = result.fetchone()
        logger.debug(f'student id - {student[0]}, student {student[1]} study in {student[2]} group')