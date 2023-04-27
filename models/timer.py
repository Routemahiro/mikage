# from sqlalchemy import Column, Integer, DateTime, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# import datetime

# Base = declarative_base()

# class Timer(Base):
#     __tablename__ = 'timer'

#     timer_id = Column(Integer, primary_key=True)
#     start_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
#     elapsed_time = Column(Integer, nullable=False)
#     is_running = Column(Boolean, nullable=False, default=False)

#     def __repr__(self):
#         return f'<Timer(timer_id={self.timer_id}, start_time={self.start_time}, elapsed_time={self.elapsed_time}, is_running={self.is_running})>'

from PySide6.QtCore import QTimer

class Timer:
    def __init__(self):
        self.duration = 25 * 60  # 25 minutes in seconds
        self.remaining_time = self.duration
        self.is_running = False

        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self._update_remaining_time)

    def _update_remaining_time(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.reset()

    def start(self):
        self.is_running = True
        self.qtimer.start(1000)

    def pause(self):
        self.is_running = False
        self.qtimer.stop()

    def reset(self):
        self.pause()
        self.remaining_time = self.duration

    def get_time_remaining(self):
        return self.remaining_time
