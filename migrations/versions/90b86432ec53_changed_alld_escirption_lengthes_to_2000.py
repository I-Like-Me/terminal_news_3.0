"""changed alld escirption lengthes to 2000

Revision ID: 90b86432ec53
Revises: fb98f0f6f4a1
Create Date: 2023-12-31 12:23:51.151700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b86432ec53'
down_revision = 'fb98f0f6f4a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('ammo_power', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('architype', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('background', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('job',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=64),
               existing_nullable=True)
        batch_op.alter_column('job_desc',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('backpack',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=50000),
               existing_nullable=True)
        batch_op.alter_column('play_notes',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=50000),
               existing_nullable=True)
        batch_op.alter_column('char_sum',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=50000),
               existing_nullable=True)

    with op.batch_alter_table('cybernetic', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('body_part',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=64),
               existing_nullable=True)

    with op.batch_alter_table('faction', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('feature', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('ladder', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('ladder_gain_5',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('ladder_gain_11',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('ladder_gain_17',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('mech', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.add_column(sa.Column('race_stat_increases', sa.String(length=2000), nullable=True))
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('rank', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=120),
               existing_nullable=True)

    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=12),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('rank', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.drop_column('race_stat_increases')

    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('mech', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)

    with op.batch_alter_table('ladder', schema=None) as batch_op:
        batch_op.alter_column('ladder_gain_17',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.alter_column('ladder_gain_11',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.alter_column('ladder_gain_5',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('feature', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('faction', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('cybernetic', schema=None) as batch_op:
        batch_op.alter_column('body_part',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=12),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('char_sum',
               existing_type=sa.String(length=50000),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)
        batch_op.alter_column('play_notes',
               existing_type=sa.String(length=50000),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)
        batch_op.alter_column('backpack',
               existing_type=sa.String(length=50000),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)
        batch_op.alter_column('job_desc',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
        batch_op.alter_column('job',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)

    with op.batch_alter_table('background', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('architype', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('ammo_power', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###
