"""create tables table

Revision ID: 48c911fc95f3
Revises: 11261d3a8154
Create Date: 2021-01-18 14:29:16.040625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48c911fc95f3'
down_revision = '11261d3a8154'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    tables_table = op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )

    op.bulk_insert(tables_table, [
        {'number': 1, 'capacity': 4},
        {'number': 2, 'capacity': 2},
        {'number': 3, 'capacity': 4},
        {'number': 4, 'capacity': 2},
        {'number': 5, 'capacity': 10},
        {'number': 6, 'capacity': 6},
        {'number': 7, 'capacity': 15},
        {'number': 8, 'capacity': 2},
        {'number': 9, 'capacity': 4},
        {'number': 10, 'capacity': 8}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tables')
    # ### end Alembic commands ###