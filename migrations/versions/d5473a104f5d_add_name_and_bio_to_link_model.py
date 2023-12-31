"""Add name and bio to Link model

Revision ID: d5473a104f5d
Revises: 
Create Date: 2023-12-18 01:02:52.048939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5473a104f5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('bio', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_column('bio')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
