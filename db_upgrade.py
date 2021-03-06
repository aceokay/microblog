# If you have database migration support, then when you are ready to release
# the new version of the app to your production server you just need to record
# a new migration, copy the migration scripts to your production server and
# run a simple script that applies the changes for you. The database upgrade
# can be done with this little Python script.

#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
