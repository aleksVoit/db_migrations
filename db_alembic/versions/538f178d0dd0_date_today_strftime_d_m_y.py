"""date.today().strftime("%d-%m-%Y")

Revision ID: 538f178d0dd0
Revises: 35c66408248f
Create Date: 2024-07-28 10:43:12.756515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '538f178d0dd0'
down_revision: Union[str, None] = '35c66408248f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
