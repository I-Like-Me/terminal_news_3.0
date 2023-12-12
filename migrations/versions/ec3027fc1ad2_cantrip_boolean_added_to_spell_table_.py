"""cantrip boolean added to spell table adder

Revision ID: ec3027fc1ad2
Revises: d2e64688ceb1
Create Date: 2023-12-12 15:27:25.377188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec3027fc1ad2'
down_revision = 'd2e64688ceb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cantrip', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.drop_column('cantrip')

    # ### end Alembic commands ###
