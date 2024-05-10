from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings


SQLALCHEMY_DATABASE_URL = "sqlite:///./booking.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
# @as_declarative()
# class Base:

#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
