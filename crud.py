import argparse
import asyncio

from connect_db import async_session
from create import create_subject, create_teacher, create_student, create_group, give_mark
from update import update_student


async def main():
    parser = argparse.ArgumentParser(description='CRUD Operations')

    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'delete'],
                        required=True, help='used CRUD actions')
    parser.add_argument('-m', '--model', choices=['Group', 'Student', 'Teacher', 'Subject', 'Mark'],
                        required=True, help='tables for CRUD operations')

    parser.add_argument('-g', '--group', type=str, help='name of Group for Student')
    parser.add_argument('-n', '--name', type=str, help='name of Person or Group')
    parser.add_argument('-i', '--id', type=int, help='id of item in table')

    args = parser.parse_args()

    print(args)

    if args.action == 'create':
        if args.model == 'Student':
            await create_student(args.name, args.group)

    if args.action == 'update':
        if args.model == 'Student':
            await update_student(args.id, args.name, args.group)


if __name__ == '__main__':
    asyncio.run(main())







