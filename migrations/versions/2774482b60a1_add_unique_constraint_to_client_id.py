"""add unique constraint to client.id

Revision ID: 2774482b60a1
Revises: 52caef8c4043
Create Date: 2014-03-16 15:39:11.074384

"""

# revision identifiers, used by Alembic.
revision = '2774482b60a1'
down_revision = '52caef8c4043'

from alembic import op
import sqlalchemy as sa
from atmcraft.model import meta



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_client_identifier'), 'client', ['identifier'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_client_identifier'), 'client')
    ### end Alembic commands ###