"""Adding department field to User table

Revision ID: 3c1a22430b4e
Revises: 1ec8077855b1
Create Date: 2013-07-15 12:24:21.483097

"""

# revision identifiers, used by Alembic.
revision = '3c1a22430b4e'
down_revision = '1ec8077855b1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('department', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'department')
    ### end Alembic commands ###