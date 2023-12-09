"""skillscores fixed

Revision ID: 6de9bed9119f
Revises: a4b9e1b029e4
Create Date: 2023-12-09 15:41:34.590719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6de9bed9119f'
down_revision = 'a4b9e1b029e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill_scores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('skilled_char', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'character', ['skilled_char'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill_scores', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('skilled_char')

    # ### end Alembic commands ###
