from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from utils.logger import logger

from config.settings import DATABASE

def get_connection_url():

    connection_url = URL.create(
        drivername=DATABASE["driver"],
        username=DATABASE["user"],
        password=DATABASE["password"],
        host=DATABASE["host"],
        port=DATABASE["port"],
        database=DATABASE["database"],
    )
    return connection_url


def create_db_engine():
    try:
        _engine = create_engine(
            get_connection_url(),
            echo=False,
            pool_size=DATABASE["pool_size"],
            max_overflow=DATABASE["max_overflow"],
            pool_timeout=DATABASE["pool_timeout"],
            pool_recycle=DATABASE["pool_recycle"],
            pool_pre_ping=True
        )
        logger.info("Database engine created successfully")
        return _engine
    except Exception as e:
        logger.error(f"Error creating database engine: {e}")
        raise

engine = create_db_engine()

# Test connection
def test_connection():
    try:
        with engine.connect() as conn:
            logger.info("Successfully connected to the database")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False