"""add foreign keys

Revision ID: 0b0386a23990
Revises: 2d272c94c4ac
Create Date: 2023-10-29 02:20:21.178879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b0386a23990'
down_revision: Union[str, None] = '2d272c94c4ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key("fk_user_phone","phone","users",["user_id"],["user_id"], ondelete="CASCADE")
    op.create_foreign_key("fk_user_address", "address", "users", ["user_id"], ["user_id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("fk_user_phone","phone")
    op.drop_constraint("fk_user_address","address")
