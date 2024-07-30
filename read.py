import asyncio
from datetime import date

import sqlalchemy.exc
from sqlalchemy import select, and_

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark

from logger import logger


async def read_student(st_id: int):
    async with async_session as session:
        stmt = (select(Student.id, Student.fullname, Group.number)
                .select_from(Student).join(Group)
                .where(Student.id == st_id)
                .group_by(Student.id, Group.number))
        result = await session.execute(stmt)
        student = result.fetchone()
        logger.debug(f'student id - {student[0]}, student {student[1]} study in {student[2]} group')
        return True


async def read_students():
    async with async_session as session:
        stmt = (select(Student.id, Student.fullname, Group.number)
                .select_from(Student).join(Group)
                .group_by(Student.id, Group.number))
        result = await session.execute(stmt)
        students = result.fetchall()
        [print(f'id - {student[0]}, name - {student[1]}, group - {student[2]}') for student in students]
        return True


async def read_student_in_group(group: str):
    async with async_session as session:
        stmt = (select(Student.id, Student.fullname, Group.number)
                .select_from(Student).join(Group)
                .where(Group.number == group)
                .group_by(Student.id, Group.number))
        result = await session.execute(stmt)
        students = result.fetchall()
        [print(f'id - {student[0]}, name - {student[1]}, group - {student[2]}') for student in students]
        return True


async def read_teacher(tr_id: int):
    async with async_session as session:
        stmt = (select(Teacher.id, Teacher.fullname)
                .select_from(Teacher)
                .where(Teacher.id == tr_id)
                .group_by(Teacher.id))
        result = await session.execute(stmt)
        teacher = result.fetchone()
        logger.debug(f'teacher id - {teacher[0]}, fullname {teacher[1]}')
        return True


async def read_teachers():
    async with async_session as session:
        stmt = (select(Teacher.id, Teacher.fullname, Subject.name)
                .select_from(Teacher)
                .join(Subject)
                .group_by(Teacher.id, Subject.name))
        result = await session.execute(stmt)
        teachers = result.fetchall()
        [logger.debug(f'teacher id - {teacher[0]}, name {teacher[1]}, teach {teacher[2]}') for teacher in teachers]
        return True


async def read_subjects():
    async with async_session as session:
        stmt = (select(Subject.id, Subject.name, Teacher.fullname)
                .select_from(Subject)
                .join(Teacher)
                .group_by(Subject.id))
        result = await session.execute(stmt)
        subjects = result.fetchall()
        [logger.debug(f'subject id - {sub[0]}, name {sub[1]}, teacher{sub[2]}') for sub in subjects]
        return True


async def read_subjects_of_teacher(teacher: str):
    async with async_session as session:
        stmt = (select(Subject.id, Subject.name, Teacher.fullname)
                .select_from(Subject)
                .join(Teacher)
                .where(Teacher.fullname == teacher)
                .group_by(Subject.id, Teacher.fullname))
        result = await session.execute(stmt)
        subjects = result.fetchall()
        [logger.debug(f'subject id - {sub[0]}, name {sub[1]}, teacher {sub[2]}') for sub in subjects]
        return True


async def read_groups():
    async with async_session as session:
        stmt = (select(Group.id, Group.number)
                .select_from(Group)
                .group_by(Group.id))
        result = await session.execute(stmt)
        subjects = result.fetchall()
        [logger.debug(f'group id - {sub[0]}, number {sub[1]}') for sub in subjects]
        return True


async def read_marks_groups(group: str):
    async with async_session as session:
        stmt = (select(Mark.note, Student.fullname, Group.number)
                .select_from(Mark)
                .join(Student)
                .join(Group)
                .where(Group.number == group)
                .group_by(Mark.id, Student.fullname, Group.id))
        result = await session.execute(stmt)
        marks = result.fetchall()
        [logger.debug(f'mark - {sub[0]}, Student {sub[1]}, Group {sub[2]}') for sub in marks]
        return True


async def read_marks_students_in_subject(student: str, subject: str):
    async with async_session as session:
        stmt = (select(Mark.note, Mark.date, Student.fullname, Subject.name)
                .select_from(Mark)
                .join(Student)
                .join(Subject)
                .where(and_(Student.fullname == student, Subject.name == subject))
                .group_by(Mark.id, Subject.id, Student.fullname))
        result = await session.execute(stmt)
        marks = result.fetchall()
        [logger.debug(f'mark - {sub[0]}, date - {sub[1]}, Student {sub[2]}, Subject {sub[3]}') for sub in marks]
        return True


async def read_marks_student(student: str):
    async with async_session as session:
        stmt = (select(Mark.note, Mark.date, Student.fullname, Subject.name)
                .select_from(Mark)
                .join(Student)
                .join(Subject)
                .where(Student.fullname == student)
                .group_by(Subject.id, Mark.note, Mark.date, Student.id)
                .order_by(Subject.id))

        result = await session.execute(stmt)
        marks = result.fetchall()
        [logger.debug(f'mark - {sub[0]}, date - {sub[1]}, Student {sub[2]}, Subject {sub[3]}') for sub in marks]
        return True
