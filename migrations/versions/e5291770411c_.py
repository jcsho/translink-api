"""empty message

Revision ID: e5291770411c
Revises: 6694d218f991
Create Date: 2021-03-29 00:52:41.546341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5291770411c'
down_revision = '6694d218f991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.Column('bus_id', sa.Integer(), nullable=True),
    sa.Column('stop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bus_id'], ['buses.id'], ),
    sa.ForeignKeyConstraint(['stop_id'], ['stops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routes')
    # ### end Alembic commands ###
