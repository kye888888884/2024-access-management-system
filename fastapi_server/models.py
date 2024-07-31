from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# id / name / is_working
class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_working = Column(Integer, nullable=False)

# idx / id / date
class Record(Base):
    __tablename__ = "record"

    idx = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("worker.id"))
    date = Column(DateTime, nullable=False)