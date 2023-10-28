"""create phone table

Revision ID: 94bfdf63430b
Revises: 0a30eea008f0
Create Date: 2023-10-25 01:00:59.088779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94bfdf63430b'
down_revision: Union[str, None] = '0a30eea008f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        "phones",
        sa.Column("phone_id", sa.Uuid, primary_key=True),
        sa.Column("type", sa.String()),
        sa.Column("number", sa.String())
    )
     op.create_foreign_key("fk_user_phone", "users", "phones", ["user_id"], ["phone_id"])


def downgrade() -> None:
    op.drop_table("phones")
