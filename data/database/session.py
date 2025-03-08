# app/db/session.py
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager
from utils.logger import logger

from data.database.connection import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ScopedSession = scoped_session(SessionLocal)

def get_db():

    db = ScopedSession()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def db_session():
    session = ScopedSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Session error: {e}")
        raise
    finally:
        session.close()