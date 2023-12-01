"""char_cls name added

Revision ID: c02fd62a078e
Revises: bead5644c0dd
Create Date: 2023-11-30 16:05:18.627489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02fd62a078e'
down_revision = 'bead5644c0dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('char_cls', schema=None) as batch_op:
        batch_op.add_column(sa.Column('char_cls', sa.String(length=64), nullable=True))
        batch_op.create_index(batch_op.f('ix_char_cls_char_cls'), ['char_cls'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('char_cls', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_char_cls_char_cls'))
        batch_op.drop_column('char_cls')

    # ### end Alembic commands ###
