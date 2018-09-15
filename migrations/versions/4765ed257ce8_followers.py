"""followers

Revision ID: 4765ed257ce8
Revises: 89fb51075d34
Create Date: 2018-09-15 15:30:23.894117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4765ed257ce8'
down_revision = '89fb51075d34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
