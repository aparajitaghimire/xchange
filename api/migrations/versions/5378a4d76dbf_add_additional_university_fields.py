"""Add additional university fields

Revision ID: 5378a4d76dbf
Revises: dc93ace81d26
Create Date: 2023-08-13 16:36:23.422462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5378a4d76dbf'
down_revision = 'dc93ace81d26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('university', schema=None) as batch_op:
        batch_op.add_column(sa.Column('academic_level', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('requirements', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('tuition', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('transcript', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('housing', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('faculties', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('dates', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('finacial_support', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('contact', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('cost', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('cost_disclaimer', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('university', schema=None) as batch_op:
        batch_op.drop_column('cost_disclaimer')
        batch_op.drop_column('cost')
        batch_op.drop_column('contact')
        batch_op.drop_column('finacial_support')
        batch_op.drop_column('dates')
        batch_op.drop_column('faculties')
        batch_op.drop_column('housing')
        batch_op.drop_column('transcript')
        batch_op.drop_column('tuition')
        batch_op.drop_column('requirements')
        batch_op.drop_column('academic_level')

    # ### end Alembic commands ###
