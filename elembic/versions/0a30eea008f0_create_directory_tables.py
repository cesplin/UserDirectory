"""create directory tables

Revision ID: 0a30eea008f0
Revises: 
Create Date: 2023-10-25 00:29:37.293410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a30eea008f0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("user_id", sa.Uuid, primary_key=True),
        sa.Column("display_name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=True),
        sa.Column("given",sa.String(),nullable=True),
        sa.Column("middle",sa.String(),nullable=True),
        sa.Column("title",sa.String(),nullable=True),
        sa.Column("suffix",sa.String(), nullable=True),
        sa.Column("division", sa.String(),nullable=True),
        sa.Column("department", sa.String(),nullable=True)
    )
    

def downgrade() -> None:
    op.drop_table("user")
    op.drop_table("address")
    op.drop_table("phone")
