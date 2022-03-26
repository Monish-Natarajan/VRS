"""img_path added to Movies

Revision ID: 16fc3c4c578e
Revises: 46fbb3b88859
Create Date: 2022-03-26 22:48:22.363821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fc3c4c578e'
down_revision = '46fbb3b88859'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('img_path', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'img_path')
    # ### end Alembic commands ###
