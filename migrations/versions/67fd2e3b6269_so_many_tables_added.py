"""so many tables added

Revision ID: 67fd2e3b6269
Revises: 90cb7e9f2883
Create Date: 2023-12-05 10:49:23.907925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67fd2e3b6269'
down_revision = '90cb7e9f2883'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cls_5e', schema=None) as batch_op:
        batch_op.add_column(sa.Column('max_num_pro_skills', sa.Integer(), nullable=True))

    with op.batch_alter_table('clsinfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('arch', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('total_hit_dice', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('cur_hit_dice', sa.String(length=64), nullable=True))
        batch_op.drop_column('learned_history')
        batch_op.drop_column('real_age')
        batch_op.drop_column('birth_name')
        batch_op.drop_column('hidden_history')
        batch_op.drop_column('age')
        batch_op.drop_column('public_history')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clsinfo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_history', sa.VARCHAR(length=5000), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('hidden_history', sa.VARCHAR(length=5000), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('birth_name', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('real_age', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('learned_history', sa.VARCHAR(length=5000), autoincrement=False, nullable=True))
        batch_op.drop_column('cur_hit_dice')
        batch_op.drop_column('total_hit_dice')
        batch_op.drop_column('arch')

    with op.batch_alter_table('cls_5e', schema=None) as batch_op:
        batch_op.drop_column('max_num_pro_skills')

    # ### end Alembic commands ###
