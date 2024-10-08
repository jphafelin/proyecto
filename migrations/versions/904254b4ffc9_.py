"""empty message

Revision ID: 904254b4ffc9
Revises: bf82f8acf98e
Create Date: 2024-10-08 13:39:14.162857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '904254b4ffc9'
down_revision = 'bf82f8acf98e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('apellido', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('rut', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('numero_telefono', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=80), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['rut'])
        batch_op.drop_constraint('administradores_id_user_fkey', type_='foreignkey')
        batch_op.drop_column('name')
        batch_op.drop_column('id_user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_user', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('administradores_id_user_fkey', 'user', ['id_user'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password')
        batch_op.drop_column('numero_telefono')
        batch_op.drop_column('rut')
        batch_op.drop_column('email')
        batch_op.drop_column('apellido')
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###
