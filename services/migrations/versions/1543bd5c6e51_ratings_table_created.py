"""ratings table created

Revision ID: 1543bd5c6e51
Revises: 
Create Date: 2021-03-13 11:05:09.451295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1543bd5c6e51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('volunteer__rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disabled_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.Column('timely_response', sa.Integer(), nullable=True),
    sa.Column('behaviour', sa.Integer(), nullable=True),
    sa.Column('feedback', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['disabled_id'], ['disabled.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('volunteer__rating')
    # ### end Alembic commands ###