"""default=date.today()

Revision ID: 74f5ca1067f6
Revises: e36c0178bece
Create Date: 2024-07-28 10:29:04.572697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74f5ca1067f6'
down_revision: Union[str, None] = 'e36c0178bece'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
