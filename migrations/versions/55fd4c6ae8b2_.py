"""empty message

Revision ID: 55fd4c6ae8b2
Revises: a0c63733e5d2
Create Date: 2018-08-06 23:35:34.202111

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '55fd4c6ae8b2'
down_revision = 'a0c63733e5d2'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification_actions', 'subject_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.String(),
                    existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification_actions', 'subject_id',
                    existing_type=sa.String(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    # ### end Alembic commands ###
