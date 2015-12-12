"""merge 11f and 1f5

Revision ID: b87f01a5ffc
Revises: 11f941b633ea, 1f5c6ab1f659
Create Date: 2015-12-12 12:39:15.252727

"""

# revision identifiers, used by Alembic.
revision = 'b87f01a5ffc'
down_revision = ('11f941b633ea', '1f5c6ab1f659')
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    pass


def downgrade():
    pass
