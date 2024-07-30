import asyncio
from datetime import date, datetime

import sqlalchemy.exc

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from sqlalchemy.future import select

from logger import logger


async def create_group(group_name: str):
    async with async_session as session:
        group = Group(number=group_name)
        session.add(group)
        await session.commit()
        logger.debug(f'created group - {group_name}')
        return True


async def create_student(fullname: str, group_number: str):
    name = fullname.split(' ')[-2:][0]
    if not name:
        return False
    async with async_session as session:
        async with session.begin():
            stmt = select(Group.id).where(Group.number == group_number)
            result = await session.execute(stmt)
            group_id = result.scalar()
            student = Student(name=name, fullname=fullname, group_id=group_id)
            session.add(student)
            await session.commit()
            logger.debug(f'created student - {fullname}')
            return True


async def create_teacher(fullname: str):
    name = fullname.split(' ')[-2:][0]
    if not name:
        return False
    async with async_session as session:
        teacher = Teacher(name=name, fullname=fullname)
        session.add(teacher)
        await session.commit()
        logger.debug(f'created teacher - {fullname}')
        return True


async def create_subject(name: str, teacher_fullname: str):
    async with async_session as session:
        async with session.begin():
            stmt = select(Teacher.id).where(Teacher.fullname == teacher_fullname)
            result = await session.execute(stmt)
            teacher_id = result.scalar()
            if not teacher_id:
                return False
            subject = Subject(name=name, teacher_id=teacher_id)
            session.add(subject)
            await session.commit()
            logger.debug(f'created subject - {name}')
            return True


async def give_mark(note: int, exam_date: str, student_fullname: str, subject_name: str):
    if not note or not exam_date or not student_fullname or not subject_name:
        return False
    async with async_session as session:
        async with session.begin():
            stmt = select(Student.id).where(Student.fullname == student_fullname)
            result = await session.execute(stmt)
            student_id = result.scalar()

            stmt = select(Subject.id).where(Subject.name == subject_name)
            result = await session.execute(stmt)
            subject_id = result.scalar()

            if not student_id or not subject_id:
                return False

            exam_date = datetime.strptime(exam_date, '%Y-%m-%d').date()
            logger.debug(f'{note}, {exam_date}, {student_id}, {subject_id}')
            mark = Mark(note=note, date=exam_date, student_id=student_id, subject_id=subject_id)
            session.add(mark)
            await session.commit()
            logger.debug(f'mark was written')
            return True


async def init_tables():
    await create_group('24-01')
    await create_student('Nathan Wilson', '23-05')
    await create_teacher('Vasil Petrovich')
    await create_subject('Python', 'Heather Davis')
    await give_mark(99, '2024-05-05', 'Nathan Wilson', 'Python')


if __name__ == '__main__':
    asyncio.run(init_tables())
