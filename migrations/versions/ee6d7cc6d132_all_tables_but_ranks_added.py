"""all tables but ranks added

Revision ID: ee6d7cc6d132
Revises: 7cb2f4f968ea
Create Date: 2023-12-07 13:00:29.056321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6d7cc6d132'
down_revision = '7cb2f4f968ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('armor_dmg_type_table')
    with op.batch_alter_table('armor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tech_level', sa.Integer(), nullable=True))

    with op.batch_alter_table('clsinfo', schema=None) as batch_op:
        batch_op.drop_column('arch')

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('tech_level', sa.Integer(), nullable=True))

    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.drop_column('martial')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('martial', sa.BOOLEAN(), autoincrement=False, nullable=True))

    with op.batch_alter_table('gear', schema=None) as batch_op:
        batch_op.drop_column('tech_level')
        batch_op.drop_column('description')

    with op.batch_alter_table('clsinfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('arch', sa.VARCHAR(length=64), autoincrement=False, nullable=True))

    with op.batch_alter_table('armor', schema=None) as batch_op:
        batch_op.drop_column('tech_level')

    op.create_table('armor_dmg_type_table',
    sa.Column('armor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('damagetype_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['armor_id'], ['armor.id'], name='armor_dmg_type_table_armor_id_fkey'),
    sa.ForeignKeyConstraint(['damagetype_id'], ['damagetype.id'], name='armor_dmg_type_table_damagetype_id_fkey'),
    sa.PrimaryKeyConstraint('armor_id', 'damagetype_id', name='armor_dmg_type_table_pkey')
    )
    # ### end Alembic commands ###
