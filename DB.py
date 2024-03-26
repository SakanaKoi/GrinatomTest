from sqlalchemy import Column, Integer, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    duration = Column(Float)
    start_number = Column(Integer)


engine = create_engine("sqlite:///bot_runs.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
