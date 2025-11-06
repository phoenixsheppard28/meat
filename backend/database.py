from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import Engine
from config import get_config, Config
from typing import Iterator


cfg = get_config()


def _init_engine(c: Config) -> Engine:
    engine = create_engine(c.DATABASE_URL)
    SQLModel.metadata.create_all(engine)
    return engine


def get_db() -> Iterator[Session]:
    engine = _init_engine(cfg)
    with Session(engine) as session:
        yield session
