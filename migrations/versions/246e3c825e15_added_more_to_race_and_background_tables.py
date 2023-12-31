"""added more to race and background tables

Revision ID: 246e3c825e15
Revises: 90b86432ec53
Create Date: 2023-12-31 15:24:54.597601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246e3c825e15'
down_revision = '90b86432ec53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('background', schema=None) as batch_op:
        batch_op.add_column(sa.Column('extra_languages_num', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('tool_pro_restrictions', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('bg_equipment', sa.String(length=100), nullable=True))

    with op.batch_alter_table('bg_pro_tool_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('background_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('bg_pro_tool_table_cls_5e_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'background', ['background_id'], ['id'])
        batch_op.drop_column('cls_5e_id')

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('finalized', sa.Boolean(), nullable=True))

    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('size', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('extra_languages_num', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('race', schema=None) as batch_op:
        batch_op.drop_column('extra_languages_num')
        batch_op.drop_column('size')
        batch_op.drop_column('value')

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_column('finalized')

    with op.batch_alter_table('bg_pro_tool_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cls_5e_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('bg_pro_tool_table_cls_5e_id_fkey', 'cls_5e', ['cls_5e_id'], ['id'])
        batch_op.drop_column('background_id')

    with op.batch_alter_table('background', schema=None) as batch_op:
        batch_op.drop_column('bg_equipment')
        batch_op.drop_column('tool_pro_restrictions')
        batch_op.drop_column('extra_languages_num')

    # ### end Alembic commands ###
