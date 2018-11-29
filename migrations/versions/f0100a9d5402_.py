"""empty message

Revision ID: f0100a9d5402
Revises: bfe14b022385
Create Date: 2018-11-29 11:20:05.699021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0100a9d5402'
down_revision = 'bfe14b022385'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('response', sa.String(length=5000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction', 'response')
    # ### end Alembic commands ###
