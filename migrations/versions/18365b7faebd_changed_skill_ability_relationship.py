"""changed skill ability relationship

Revision ID: 18365b7faebd
Revises: 74c7d0b4ea31
Create Date: 2024-01-03 09:32:42.067107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18365b7faebd'
down_revision = '74c7d0b4ea31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.drop_constraint('skill_ability_fkey', type_='foreignkey')
        batch_op.drop_column('ability')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ability', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('skill_ability_fkey', 'ability', ['ability'], ['name'])

    # ### end Alembic commands ###
