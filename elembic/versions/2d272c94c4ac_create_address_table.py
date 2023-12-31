"""create address table

Revision ID: 2d272c94c4ac
Revises: 94bfdf63430b
Create Date: 2023-10-25 01:01:08.913234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d272c94c4ac'
down_revision: Union[str, None] = '94bfdf63430b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("addr_id", sa.Uuid, primary_key=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("house_number", sa.String(), nullable=True),
        sa.Column("street", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("state", sa.String(), nullable=True),
        sa.Column("user_id", sa.Uuid, unique=True, nullable=False)
    )
    op.create_index("ik_addr_user","address",["user_id"])

def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("addresses")
    op.drop_table("phones")
