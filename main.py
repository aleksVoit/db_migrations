import argparse
import asyncio

from create import create_subject, create_teacher, create_student, create_group, give_mark
from update import update_student
from read import read_student
from delete import delete_student

from logger import logger


async def main():
    parser = argparse.ArgumentParser(description='CRUD Operations')

    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'delete'],
                        required=True, help='used CRUD actions')
    parser.add_argument('-m', '--model', choices=['Group', 'Student', 'Teacher', 'Subject', 'Mark'],
                        required=True, help='tables for CRUD operations')

    parser.add_argument('-g', '--group', type=str, help='name of Group for Student')
    parser.add_argument('-d', '--date', type=str, help='date of exam')
    parser.add_argument('-n', '--name', type=str, help='name of Person or Group')
    parser.add_argument('-s', '--student', type=str, help='fullname of Student')
    parser.add_argument('-t', '--teacher', type=str, help='fullname of Teacher')
    parser.add_argument('-j', '--subject', type=str, help='name Subject')
    parser.add_argument('-i', '--id', type=int, help='id of item in table')

    args = parser.parse_args()

    print(args)

    try:
        if args.action == 'create':
            if args.model == 'Student':
                await create_student(args.name, args.group)
            if args.model == 'Teacher':
                await create_teacher(args.name)

        if args.action == 'update':
            if args.model == 'Student':
                await update_student(args.id, args.name, args.group)

        if args.action == 'list':
            if args.model == 'Student':
                await read_student(args.id)

        if args.action == 'delete':
            if args.model == 'Student':
                await delete_student(args.id)

    except IOError as err:
        logger.debug(f'{err}')
        help()


if __name__ == '__main__':
    asyncio.run(main())







