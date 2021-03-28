"""empty message

Revision ID: 6694d218f991
Revises: 
Create Date: 2021-03-28 23:42:52.448401

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geography


# revision identifiers, used by Alembic.
revision = '6694d218f991'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicleId', sa.Integer(), nullable=True),
    sa.Column('location', Geography(geometry_type='POINT', srid=4326, from_text='ST_GeogFromText', name='geography'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('location', Geography(geometry_type='POINT', srid=4326, from_text='ST_GeogFromText', name='geography'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('stops')
    op.drop_table('buses')
    # ### end Alembic commands ###