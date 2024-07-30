import argparse
import asyncio
from datetime import datetime, date

from create import create_subject, create_teacher, create_student, create_group, give_mark
from update import update_student, update_teacher, update_subject, update_group
from read import (read_student, read_students, read_teacher, read_student_in_group, read_teachers,
                  read_subjects, read_subjects_of_teacher, read_groups, read_marks_groups,
                  read_marks_students_in_subject, read_marks_student, )
from delete import delete_student, delete_teacher, delete_group, delete_subject
from tables_delete import delete_tables, delete_marks, delete_groups, delete_students, delete_subjects, delete_teachers

from logger import logger


def confirm(prompt: str) -> bool:
    """Запрашивает подтверждение у пользователя."""
    while True:
        response = input(f"{prompt} [y/n]: ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Пожалуйста, введите 'y' для подтверждения или 'n' для отмены.")

async def main():
    parser = argparse.ArgumentParser(description='CRUD Operations')

    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'delete'],
                        required=True, help='used CRUD actions')
    parser.add_argument('-m', '--model', choices=['Group', 'Student', 'Teacher', 'Subject', 'Mark'],
                        required=True, help='tables for CRUD operations')

    parser.add_argument('-g', '--group', type=str, help='name of Group for Student "20-02"')
    parser.add_argument('-d', '--date', type=str, help='date of exam "2024-02-24"')
    parser.add_argument('-n', '--name', type=str, help='name of Person or Group "Vasyl Pupkin" or "20-02"')
    parser.add_argument('-s', '--student', type=str, help='fullname of Student "Vasyl Pupkin"')
    parser.add_argument('-t', '--teacher', type=str, help='fullname of Teacher "Vasyl Pupkin"')
    parser.add_argument('-j', '--subject', type=str, help='name Subject "Mathematics"')
    parser.add_argument('-i', '--id', type=int, help='id of item in table')
    parser.add_argument('-b', '--grade', type=int, help='grade on exam in range between 0 and 100')

    args = parser.parse_args()

    try:
        res = None
        if args.action == 'create':
            if args.model == 'Group':
                res = await create_group(args.name)
            if args.model == 'Teacher':
                res = await create_teacher(args.name)
            if args.model == 'Student':
                res = await create_student(args.name, args.group)
            if args.model == 'Subject':
                res = await create_subject(args.name, args.teacher)
            if args.model == 'Mark':
                res = await give_mark(args.grade, args.date, args.student, args.subject)

        if args.action == 'list':
            if args.model == 'Student' and args.id:
                res = await read_student(args.id)
            elif args.model == 'Student' and args.group:
                res = await read_student_in_group(args.group)
            elif args.model == 'Student':
                res = await read_students()

            if args.model == 'Teacher' and args.id:
                res = await read_teacher(args.id)
            elif args.model == 'Teacher':
                res = await read_teachers()

            if args.model == 'Subject' and args.teacher:
                res = await read_subjects_of_teacher(args.teacher)
            elif args.model == 'Subject':
                res = await read_subjects()

            if args.model == 'Group':
                res = await read_groups()

            if args.model == 'Mark' and args.group:
                res = await read_marks_groups(args.group)
            elif args.model == 'Mark' and args.student and args.subject:
                logger.debug('in student subject')
                res = await read_marks_students_in_subject(args.student, args.subject)
            elif args.model == 'Mark' and args.student:
                logger.debug('in student')
                res = await read_marks_student(args.student)

        if args.action == 'update':
            if args.model == 'Student':
                res = await update_student(args.id, args.name, args.group)
            if args.model == 'Teacher':
                res = await update_teacher(args.id, args.name)
            if args.model == 'Subject':
                res = await update_subject(args.id, args.name, args.teacher)
            if args.model == 'Group':
                res = await update_group(args.id, args.name)

        if args.action == 'delete':
            if args.model == 'Student' and args.id:
                res = await delete_student(args.id)
            elif args.model == 'Student':
                if confirm('Delete all students? '):
                    res = await delete_students()
            if args.model == 'Teacher' and args.id:
                res = await delete_teacher(args.id)
            elif args.model == 'Teacher':
                if confirm('Delete all Teachers? '):
                    res = await delete_teachers()
            if args.model == 'Group' and args.id:
                res = await delete_group(args.id)
            elif args.model == 'Group':
                if confirm('Delete all groups? '):
                    res = await delete_groups()
            if args.model == 'Subject' and args.id:
                res = await delete_subject(args.id)
            elif args.model == 'Subject':
                if confirm('Delete all subjects? '):
                    res = await delete_subjects()

        if not res:
            raise TypeError('not correct arguments')

    except (IOError, TypeError) as err:
        logger.debug(f'{err}')
        parser.print_help()


if __name__ == '__main__':
    asyncio.run(main())







