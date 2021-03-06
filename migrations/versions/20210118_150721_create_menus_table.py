"""create menus table

Revision ID: dfbf3b5f15ee
Revises: e0409fe15b8b
Create Date: 2021-01-18 15:07:21.205379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfbf3b5f15ee'
down_revision = 'e0409fe15b8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    menus_table = op.create_table('menus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(menus_table, [
        {'name': 'Breakfast'},
        {'name': 'Lunch'},
        {'name': 'Dinner'},
        {'name': 'Happy Hour'},
        {'name': 'Weekend Brunch'},
        {'name': 'Kids'},
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menus')
    # ### end Alembic commands ###
