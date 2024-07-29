import asyncio
from datetime import date

from connect_db import async_session
from models import Group, Student, Teacher, Subject, Mark
from faker import Faker
from random import randint, choice, sample
from sqlalchemy.future import select

from create import create_teacher, create_subject, create_group, create_student, give_mark

faker = Faker()


async def init_groups(quantity: int):
    groups = []
    while True:
        year = randint(19, 23)
        number = f'0{randint(1, 5)}'
        group_name = f'{year}-{number}'
        if group_name not in groups:
            groups.append(group_name)
            await create_group(group_name)
        if len(groups) == quantity:
            break


async def init_students(quantity: int):
    async with async_session as session:
        stmt = select(Group.number)
        result = await session.execute(stmt)
        groups = result.scalars().all()
    for _ in range(quantity):
        full_name = faker.name()
        await create_student(full_name, choice(groups))


async def init_teachers(quantity: int):
    for _ in range(quantity):
        full_name = faker.name()
        await create_teacher(full_name)


async def init_subjects(quantity: int):
    subjects_items = ["Mathematics", "Physics", "Chemistry", "Biology",
                      "Computer Science", "History", "Philosophy",
                      "Linguistics", "Literature", "Economics", "Psychology",
                      "Sport", "Programming", "Theory of Automation", "Nature",
                      "English", "Deutsch", "Geography", "Power plants"]
    subjects = sample(subjects_items, quantity)
    async with async_session as session:
        stmt = select(Teacher.fullname)
        teachers = await session.execute(stmt)
        teachers_names = teachers.scalars().all()
    used_names = []
    for subject in subjects:
        while True:
            t_name = choice(teachers_names)
            if t_name not in used_names:
                used_names.append(t_name)
                await create_subject(subject, t_name)
                break
            elif len(used_names) == len(teachers_names):
                await create_subject(subject, choice(teachers_names))
                break


async def init_marks(quantity: int):
    async with async_session as session:

        stmt = select(Student)
        result = await session.execute(stmt)
        students = result.scalars().all()

        stmt = select(Subject)
        result = await session.execute(stmt)
        subjects = result.scalars().all()

    used_subjects = []

    for mark in range(quantity):
        exam_date = generate_random_work_day()
        subject = choose_subject(subjects, used_subjects)
        for student in students:
            await give_mark(randint(1, 100), exam_date, student.fullname, subject.name)


def choose_subject(subjects, used_subjects):
    sub = choice(subjects)
    if sub not in used_subjects:
        return sub
    elif len(subjects) == len(used_subjects):
        used_subjects = []
        return choose_subject(subjects, used_subjects)
    else:
        return choose_subject(subjects, used_subjects)


start_day = date(2024, 1, 2)
end_day = date(2024, 6, 15)


def generate_random_work_day():
    while True:
        random_date = faker.date_between(start_day, end_day)
        if random_date.weekday() < 5:
            return random_date


async def init_tables():
    await init_groups(3)
    print('groups finished')
    await init_students(50)
    print('students finished')
    await init_teachers(5)
    print('teachers finished')
    await init_subjects(7)
    print('subjects finished')
    await init_marks(20)
    print('marks finished')

if __name__ == '__main__':
    asyncio.run(init_tables())
