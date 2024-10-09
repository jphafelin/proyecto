"""empty message

Revision ID: 58ab563192a8
Revises: 9ee1a0c0123c
Create Date: 2024-10-09 01:04:28.284500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ab563192a8'
down_revision = '9ee1a0c0123c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('evento', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=1000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('evento', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=sa.String(length=1000),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###