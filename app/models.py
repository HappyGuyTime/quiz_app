from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class QuizModel(Base):
    __tablename__ = 'quiz_data'

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)
    question = Column(String)
    created_at = Column(DateTime)