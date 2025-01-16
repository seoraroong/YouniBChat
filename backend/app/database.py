from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:password@localhost:5432/younibchat_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB 연결 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()