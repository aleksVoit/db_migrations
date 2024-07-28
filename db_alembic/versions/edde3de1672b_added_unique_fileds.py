"""added unique fileds

Revision ID: edde3de1672b
Revises: d8cd59a925c3
Create Date: 2024-07-28 15:04:22.902006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edde3de1672b'
down_revision: Union[str, None] = 'd8cd59a925c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('groups_number_key', 'groups', ['number'])
    op.create_unique_constraint('students_fullname_key', 'students', ['fullname'])
    op.create_unique_constraint('subjects_name_key', 'subjects', ['name'])
    op.create_unique_constraint('teachers_name_key', 'teachers', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('teachers_name_key', 'teachers', type_='unique')
    op.drop_constraint('subjects_name_key', 'subjects', type_='unique')
    op.drop_constraint('students_fullname_key', 'students', type_='unique')
    op.drop_constraint('groups_number_key', 'groups', type_='unique')
    # ### end Alembic commands ###