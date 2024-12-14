"""Rename column in students table

Revision ID: f0b2482b75c1
Revises: 791279dd0760
Create Date: 2024-12-14 15:02:17.244424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0b2482b75c1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'birthday', new_column_name = 'date_of_birth')


def downgrade() -> None:
    op.alter_column('students', 'date_of_birth', new_column_name = 'birthday')
