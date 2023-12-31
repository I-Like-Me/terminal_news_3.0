"""char_know changed

Revision ID: 5675e6ebd59a
Revises: 0ddd9d102b30
Create Date: 2023-12-09 16:15:02.724245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5675e6ebd59a'
down_revision = '0ddd9d102b30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('char_know', schema=None) as batch_op:
        batch_op.alter_column('learner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('subject_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_index('ix_char_know_char_char')
        batch_op.drop_column('char_char')
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('char_know', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('char_char', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.create_index('ix_char_know_char_char', ['char_char'], unique=False)
        batch_op.alter_column('subject_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('learner_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
