"""empty message

Revision ID: 41d5cc9288a2
Revises: 33558df36a61
Create Date: 2023-06-27 20:45:49.335780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41d5cc9288a2'
down_revision = '33558df36a61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=False))
        batch_op.drop_constraint('user_first_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('first_name')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_first_name_key', ['first_name'])
        batch_op.drop_column('username')

    # ### end Alembic commands ###