"""Create one to many relaatinship between groups table and playlists table

Revision ID: 2f1c22fb90f5
Revises: a9f4e32db4b6
Create Date: 2017-11-07 16:31:21.026899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f1c22fb90f5'
down_revision = 'a9f4e32db4b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playlists', sa.Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'playlists', 'groups', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'playlists', type_='foreignkey')
    op.drop_column('playlists', 'group_id')
    # ### end Alembic commands ###