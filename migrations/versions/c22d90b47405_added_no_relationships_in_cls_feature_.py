"""added no relationships in cls, feature, bg, and char

Revision ID: c22d90b47405
Revises: 246e3c825e15
Create Date: 2024-01-02 10:37:00.892768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22d90b47405'
down_revision = '246e3c825e15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race_pro_weap_table')
    with op.batch_alter_table('ammo_power', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('armor', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('cybernetic', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('mech', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('mech', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('cybernetic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('armor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('ammo_power', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.INTEGER(), autoincrement=False, nullable=True))

    op.create_table('race_pro_weap_table',
    sa.Column('race_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('weapon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['race_id'], ['race.id'], name='race_pro_weap_table_race_id_fkey'),
    sa.ForeignKeyConstraint(['weapon_id'], ['weapon.id'], name='race_pro_weap_table_weapon_id_fkey'),
    sa.PrimaryKeyConstraint('race_id', 'weapon_id', name='race_pro_weap_table_pkey')
    )
    # ### end Alembic commands ###