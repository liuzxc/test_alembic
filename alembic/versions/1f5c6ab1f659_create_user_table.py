"""create user table

Revision ID: 1f5c6ab1f659
Revises: 22828b872b43
Create Date: 2015-12-12 12:27:17.634281

"""

# revision identifiers, used by Alembic.
revision = '1f5c6ab1f659'
down_revision = '22828b872b43'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('user')
