"""empty message

Revision ID: b53aa6ec8a93
Revises: ff8590045e2f
Create Date: 2023-06-08 16:46:07.575729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b53aa6ec8a93'
down_revision = 'ff8590045e2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_time', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('update_time', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_column('update_time')
        batch_op.drop_column('create_time')

    # ### end Alembic commands ###