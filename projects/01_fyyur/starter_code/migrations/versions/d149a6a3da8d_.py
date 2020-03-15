"""empty message

Revision ID: d149a6a3da8d
Revises: e8588c822895
Create Date: 2020-03-14 11:03:36.401766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd149a6a3da8d'
down_revision = 'e8588c822895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Artist_past_shows_fkey', 'Artist', type_='foreignkey')
    op.drop_constraint('Artist_upcoming_shows_fkey', 'Artist', type_='foreignkey')
    op.add_column('PastShow', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('PastShow', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'PastShow', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'PastShow', 'Venue', ['venue_id'], ['id'])
    op.drop_constraint('Venue_upcoming_shows_fkey', 'Venue', type_='foreignkey')
    op.drop_constraint('Venue_past_shows_fkey', 'Venue', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('Venue_past_shows_fkey', 'Venue', 'PastShow', ['past_shows'], ['id'])
    op.create_foreign_key('Venue_upcoming_shows_fkey', 'Venue', 'UpcomingShow', ['upcoming_shows'], ['id'])
    op.drop_constraint(None, 'PastShow', type_='foreignkey')
    op.drop_constraint(None, 'PastShow', type_='foreignkey')
    op.drop_column('PastShow', 'venue_id')
    op.drop_column('PastShow', 'artist_id')
    op.create_foreign_key('Artist_upcoming_shows_fkey', 'Artist', 'UpcomingShow', ['upcoming_shows'], ['id'])
    op.create_foreign_key('Artist_past_shows_fkey', 'Artist', 'PastShow', ['past_shows'], ['id'])
    # ### end Alembic commands ###
