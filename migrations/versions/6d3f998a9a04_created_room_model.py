"""Created Room Model

Revision ID: 6d3f998a9a04
Revises: 3eb55fe6e9f0
Create Date: 2021-05-05 14:05:28.639193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d3f998a9a04'
down_revision = '3eb55fe6e9f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(length=255), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('cost', sa.String(length=255), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('classification')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rooms')
    # ### end Alembic commands ###
