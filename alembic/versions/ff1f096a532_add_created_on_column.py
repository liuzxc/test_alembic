"""add created_on column

Revision ID: ff1f096a532
Revises: b87f01a5ffc
Create Date: 2015-12-12 12:54:21.540409

"""

# revision identifiers, used by Alembic.
revision = 'ff1f096a532'
down_revision = 'b87f01a5ffc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('created_on', sa.DateTime))


def downgrade():
    op.drop_column('user', 'created_on')
