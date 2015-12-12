"""create account table

Revision ID: 1ddccadebd5e
Revises:
Create Date: 2015-12-12 11:39:57.888118

"""

# revision identifiers, used by Alembic.
revision = '1ddccadebd5e'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
