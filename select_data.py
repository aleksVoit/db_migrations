import asyncio

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from sqlalchemy import delete, select, distinct, func, desc
from sqlalchemy.sql import text


async def select_1():
    """
    to find 5 students with the highest average note at all subjects
    """
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


async def main():
    await select_1()
    await select_2('Sport')
    await select_3('Sport')
    await select_4()
    await select_5('Sarah Shelton')
    await select_6('23-05')
    await select_7('Sport', '23-05')
    await select_8('Sarah Shelton')
    await select_9('Melissa Larsen')
    await select_10('Heather Davis', 'Nathan Wilson')

if __name__ == '__main__':
    asyncio.run(main())
