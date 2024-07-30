import asyncio

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from sqlalchemy import select, func, desc, and_

from logger import logger


async def select_1():
    """
    to find 5 students with the highest average note at all subjects
    """
    logger.debug('select 1')
    async with async_session as session:
        stmt = select(Student.fullname, func.round(func.avg(Mark.note), 2).label('avg_note')
                      ).select_from(Mark).join(Student).group_by(Student.id).order_by(desc('avg_note')).limit(5)
        result = await session.execute(stmt)
        students = result.fetchall()
        [print(student) for student in students]


async def select_2(subject: str):
    """
    find a student with the highest note at specific subject
    """
    logger.debug('select 2')
    async with async_session as session:
        stmt = select(
            Student.fullname,
            Subject.name,
            func.round(func.max(Mark.note), 2).label('max_note')
        ).select_from(Mark).join(Student).join(Subject).where(
            Subject.name == subject
        ).group_by(
            Student.id, Subject.id
        ).order_by(
            desc('max_note')
        )

        result = await session.execute(stmt)
        student = result.fetchone()
        print(student)


async def select_3(subject: str):
    """
    to find the average note in groups in specific subject(groups, marks, subjects)
    """
    logger.debug('select 3')
    async with async_session as session:
        stmt = select(
            Group.number,
            Subject.name,
            func.round(func.avg(Mark.note), 2).label('avg_group_note')
        ).select_from(Mark).join(Student).join(Group).join(Subject).where(
            Subject.name == subject
        ).group_by(
            Group.id, Subject.id
        ).order_by(
            desc('avg_group_note')
        )

        result = await session.execute(stmt)
        groups_avg = result.fetchall()
        print(groups_avg)


async def select_4():
    """
    to find the average note in all groups at all subjects
    """
    logger.debug('select 4')
    async with async_session as session:
        stmt = select(
            func.round(func.avg(Mark.note), 2).label('avg_note_in_school')
        ).select_from(Mark)

        result = await session.execute(stmt)
        avg_note_in_school = result.fetchone()
        print(avg_note_in_school)


async def select_5(teacher: str):
    """
    to find list of subjects which specific lektor (subjects, lektors)
    """
    logger.debug('select 5')
    async with async_session as session:
        stmt = select(
            Subject.name,
            Teacher.fullname.label('teacher')
        ).select_from(Subject).join(Teacher).where(
            Teacher.fullname == teacher
        )
        result = await session.execute(stmt)
        subjects = result.fetchall()
        print(subjects)


async def select_6(group: str):
    """
    to find list of students in specific group
    """
    logger.debug('select 6')
    async with async_session as session:
        stmt = select(
            Student.fullname,
            Group.number
        ).select_from(Student).join(Group).where(
            Group.number == group
        ).order_by(
            Student.fullname
        )

        result = await session.execute(stmt)
        subjects = result.fetchall()
        print(subjects)


async def select_7(subject: str, group: str):
    """
    to find student's marks of specific subject in specific group
    """
    logger.debug('select 7')
    async with async_session as session:
        stmt = select(
            Student.fullname,
            Mark.note,
            Mark.date
        ).select_from(Mark).join(Student).join(Group).join(Subject).where(
            Subject.name == subject,
            Group.number == group
        ).group_by(

            Mark.date,
            Mark.note,
            Student.fullname,
        ).order_by(
            Student.fullname
        )

        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def select_8(teacher: str):
    """
    to find an average note which gives specified lektor at his subjects
    """
    logger.debug('select 8')
    async with async_session as session:
        stmt = select(
            Teacher.fullname,
            Subject.name,
            func.round(func.avg(Mark.note), 2).label('avg_note')
        ).select_from(Mark).join(Subject).join(Teacher).where(
            Teacher.fullname == teacher
        ).group_by(
            Teacher.fullname,
            Subject.name
        )

        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def select_9(student: str):
    """
    to find the list of subjects which attend a specific student
    """
    logger.debug('select 9')
    async with async_session as session:
        stmt = select(
            Student.fullname,
            Subject.name
        ).select_from(Mark).join(Subject).join(Student).where(
            Student.fullname == student
        ).group_by(
            Student.fullname,
            Subject.name
        )

        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def select_10(teacher: str, student: str):
    """
    to find the list of subjects which specific teacher teach specific student
    """
    logger.debug('select 10')
    async with async_session as session:
        stmt = select(
            Subject.name,
            Student.fullname,
            Teacher.fullname
        ).select_from(Mark).join(Subject).join(Teacher).join(Student).where(
            Teacher.fullname == teacher,
            Student.fullname == student
        ).group_by(
            Subject.name,
            Teacher.fullname,
            Student.fullname
        )

        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def select_1add(teacher: str, student: str):
    """
    to find the average note which specific teacher gives to the specific student
    """
    logger.debug('select 1add')
    async with async_session as session:
        stmt = select(
            func.round(func.avg(Mark.note), 2).label('avg_note'),
            Teacher.fullname.label('teacher'),
            Student.fullname.label('student'),
        ).select_from(Mark).join(Subject).join(Teacher).join(Student).where(
            Teacher.fullname == teacher,
            Student.fullname == student
        ).group_by(
            Teacher.fullname,
            Student.fullname
        )

        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def select_2add(group: str, subject: str):
    """
    to find the marks of students of specific group at specific subject on last lecture
    """
    logger.debug('select 2add')
    async with async_session as session:
        stmt = select(
            func.max(Mark.date)
        ).join(Subject).join(Student).join(Group).where(
            Group.number == group,
            Subject.name == subject
        )
        result = await session.execute(stmt)
        last_exam = result.fetchone()[0]

        stmt = select(
            Mark.note,
            Student.fullname.label('student'),
            Mark.date,
            Subject.name,
            Group.number
        ).select_from(Mark).join(Student).join(Group).join(Subject).where(
            and_(Mark.date == last_exam, Subject.name == subject, Group.number == group)
        ).group_by(
            Mark.id,
            Student.id,
            Mark.date,
            Subject.name,
            Group.number
        ).order_by(
            Student.fullname
        )
        result = await session.execute(stmt)
        rows = result.fetchall()
        [print(row) for row in rows]


async def main():
    await select_1()
    # await select_2('Biology')
    # await select_3('Biology')
    # await select_4()
    # await select_5('Cristina Brown')
    # await select_6('22-04')
    # await select_7('Biology', '22-04')
    # await select_8('Justin Fuentes')
    # await select_9('Mindy Moore')
    # await select_10('William Powell', 'Douglas Flores')
    # await select_1add('William Powell', 'Douglas Flores')
    # await select_2add('22-04', 'Biology')

if __name__ == '__main__':
    asyncio.run(main())
