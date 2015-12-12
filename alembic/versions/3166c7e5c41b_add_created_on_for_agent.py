"""add created_on for agent

Revision ID: 3166c7e5c41b
Revises: b87f01a5ffc
Create Date: 2015-12-12 12:57:14.672875

"""

# revision identifiers, used by Alembic.
revision = '3166c7e5c41b'
down_revision = 'b87f01a5ffc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agent', sa.Column('created_on', sa.DateTime))

def downgrade():
    op.drop_column('agent', 'created_on')