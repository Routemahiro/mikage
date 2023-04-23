from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PomodoroSettings(Base):
    __tablename__ = 'pomodoro_settings'
    
    id = Column(Integer, primary_key=True)
    work_time = Column(Integer, nullable=False, default=25)
    break_time = Column(Integer, nullable=False, default=5)

    def __repr__(self):
        return f'<PomodoroSettings(work_time={self.work_time}, break_time={self.break_time})>'