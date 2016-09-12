from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
interests = Table('interests', post_meta,
    Column('_id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('books', String(length=10)),
    Column('movies', String(length=10)),
    Column('tvshows', String(length=10)),
    Column('food', String(length=10)),
    Column('hobbies', String(length=10)),
    Column('hate', String(length=10)),
    Column('dreams', String(length=10)),
    Column('dreamcity', String(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['interests'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['interests'].drop()
