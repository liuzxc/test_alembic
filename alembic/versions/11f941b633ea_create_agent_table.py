"""create agent table

Revision ID: 11f941b633ea
Revises: 22828b872b43
Create Date: 2015-12-12 12:30:10.781115

"""

# revision identifiers, used by Alembic.
revision = '11f941b633ea'
down_revision = '22828b872b43'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'agent',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('agent')
