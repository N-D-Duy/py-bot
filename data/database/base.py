from sqlalchemy.ext.declarative import declarative_base
from utils.logger import logger
Base = declarative_base()

def init_db(_engine):

    try:

        from data.schemas.user import User
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=_engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise