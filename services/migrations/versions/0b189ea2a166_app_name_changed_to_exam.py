"""app name changed to exam

Revision ID: 0b189ea2a166
Revises: 1543bd5c6e51
Create Date: 2021-03-13 20:25:23.714196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b189ea2a166'
down_revision = '1543bd5c6e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_name', sa.Text(), nullable=True),
    sa.Column('exam_date', sa.String(length=64), nullable=True),
    sa.Column('exam_start_time', sa.String(length=64), nullable=True),
    sa.Column('exam_end_time', sa.String(length=64), nullable=True),
    sa.Column('exam_centre_addr', sa.Text(), nullable=True),
    sa.Column('exam_city', sa.String(length=64), nullable=True),
    sa.Column('exam_area_pincode', sa.Integer(), nullable=True),
    sa.Column('skills_preference', sa.Text(), nullable=True),
    sa.Column('gender_preference', sa.String(length=20), nullable=True),
    sa.Column('language_preference', sa.String(length=128), nullable=True),
    sa.Column('disabled_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disabled_id'], ['disabled.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('application')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('exam_name', sa.TEXT(), nullable=True),
    sa.Column('exam_date', sa.VARCHAR(length=64), nullable=True),
    sa.Column('exam_start_time', sa.VARCHAR(length=64), nullable=True),
    sa.Column('exam_end_time', sa.VARCHAR(length=64), nullable=True),
    sa.Column('exam_centre_addr', sa.TEXT(), nullable=True),
    sa.Column('exam_city', sa.VARCHAR(length=64), nullable=True),
    sa.Column('exam_area_pincode', sa.INTEGER(), nullable=True),
    sa.Column('skills_preference', sa.TEXT(), nullable=True),
    sa.Column('gender_preference', sa.VARCHAR(length=20), nullable=True),
    sa.Column('language_preference', sa.VARCHAR(length=128), nullable=True),
    sa.Column('disabled_id', sa.INTEGER(), nullable=True),
    sa.Column('volunteer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['disabled_id'], ['disabled.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('exam')
    # ### end Alembic commands ###