"""empty message

Revision ID: 56e51691636d
Revises: 6f1b593cd24f
Create Date: 2021-06-29 15:22:26.629899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e51691636d'
down_revision = '6f1b593cd24f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id')
    # ### end Alembic commands ###
