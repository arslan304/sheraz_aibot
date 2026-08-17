# ==============================================================
# DATABASE ENGINE & CONNECTION MANAGEMENT
# ==============================================================
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Production SQL Database (Local testing ke liye auto-create SQLite DB file)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./enterprise_ai_hub.db")

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    # High-Performance Connection Pooling
    engine = create_engine(
        DATABASE_URL,
        pool_size=20,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=1800
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI Database Session Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()