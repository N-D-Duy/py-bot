from fastapi import FastAPI
import uvicorn
from utils.logger import logger
from data.schemas.user import User, UserCreate
from data.database import test_connection, init_db, engine, db_session
from sqlalchemy import text

app = FastAPI()


@app.get("/users")
async def get_users():
    with db_session() as session:
        users = session.query(User).all()
        return users

@app.post("/users")
async def create_user(user_data: UserCreate):
    with db_session() as session:
        user = User(
            platform_id=user_data.platform_id,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            is_active=user_data.is_active
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def setup_database():
    if test_connection():
        logger.info("Database connection test passed")
        init_db(engine)
        return True
    else:
        logger.error("Database connection test failed")
        return False


def test_session():
    try:
        with db_session() as session:
            result = session.execute(text("SHOW TABLES")).fetchall()
            logger.info(f"Database tables: {result}")
        return True
    except Exception as e:
        logger.error(f"Session test failed: {e}")
        return False



if __name__ == "__main__":
    logger.info("Setting up database connection...")
    if setup_database():
        logger.info("Database setup successful")

        # Test session
        if test_session():
            logger.info("Session test successful")
        else:
            logger.error("Session test failed")
    else:
        logger.error("Database setup failed")
    uvicorn.run(app, host="127.0.0.1", port=8000)
