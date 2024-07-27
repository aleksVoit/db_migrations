"""added_relationships

Revision ID: 7024d130f39a
Revises: c8042e592b72
Create Date: 2024-07-27 11:28:02.071783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7024d130f39a'
down_revision: Union[str, None] = 'c8042e592b72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('marks_subject_id_fkey', 'marks', type_='foreignkey')
    op.drop_constraint('marks_student_id_fkey', 'marks', type_='foreignkey')
    op.create_foreign_key(None, 'marks', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'marks', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('subjects_teacher_id_fkey', 'subjects', type_='foreignkey')
    op.create_foreign_key(None, 'subjects', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.create_foreign_key('subjects_teacher_id_fkey', 'subjects', 'teachers', ['teacher_id'], ['id'])
    op.drop_constraint(None, 'marks', type_='foreignkey')
    op.drop_constraint(None, 'marks', type_='foreignkey')
    op.create_foreign_key('marks_student_id_fkey', 'marks', 'students', ['student_id'], ['id'])
    op.create_foreign_key('marks_subject_id_fkey', 'marks', 'subjects', ['subject_id'], ['id'])
    # ### end Alembic commands ###