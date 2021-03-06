"""new about_me field in user model

Revision ID: e1bd420115cc
Revises: d4bfe7b7581a
Create Date: 2019-11-08 20:55:53.358328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1bd420115cc'
down_revision = 'd4bfe7b7581a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
