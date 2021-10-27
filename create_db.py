# run with python to create new database

from database import Base, engine
Base.metadata.create_all(engine)