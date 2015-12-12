"""Add a column

Revision ID: 22828b872b43
Revises: 1ddccadebd5e
Create Date: 2015-12-12 11:51:32.784581

"""

# revision identifiers, used by Alembic.
revision = '22828b872b43'
down_revision = '1ddccadebd5e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
