# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Task(Base):
#     __tablename__ = 'task'

#     task_id = Column(Integer, primary_key=True)
#     task_name = Column(String, nullable=False)
#     priority = Column(Integer, nullable=False)
#     is_completed = Column(Boolean, nullable=False, default=False)

#     def __repr__(self):
#         return f'<Task(task_id={self.task_id}, task_name={self.task_name}, priority={self.priority}, is_completed={self.is_completed})>'
