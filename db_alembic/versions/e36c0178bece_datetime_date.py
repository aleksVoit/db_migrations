"""DateTime -> Date

Revision ID: e36c0178bece
Revises: 404e8af4ba94
Create Date: 2024-07-27 17:13:56.940964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e36c0178bece'
down_revision: Union[str, None] = '404e8af4ba94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
