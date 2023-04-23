from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Timer(Base):
    __tablename__ = 'timer'

    timer_id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    elapsed_time = Column(Integer, nullable=False)
    is_running = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Timer(timer_id={self.timer_id}, start_time={self.start_time}, elapsed_time={self.elapsed_time}, is_running={self.is_running})>'
