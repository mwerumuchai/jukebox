"""Update playlists table to have a column for the playlist image path

Revision ID: a9f4e32db4b6
Revises: c5d90b17533f
Create Date: 2017-11-07 12:51:40.335139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9f4e32db4b6'
down_revision = 'c5d90b17533f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playlists', sa.Column('image_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('playlists', 'image_path')
    # ### end Alembic commands ###
