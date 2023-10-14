from typing import List, Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import QuizModel


db_url = 'postgresql://user:qwerty@postgres:5432/quiz_db'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)


def add_quiz_data_in_db(quizzes: List[Dict]) -> None:
    '''Adds entries to the database from the list of quizzes.'''
    with Session() as session:
        data_list = [
            {
                'id': quiz_data.get('id'),
                'answer': quiz_data.get('answer'),
                'question': quiz_data.get('question'),
                'created_at': quiz_data.get('created_at')
            }
            for quiz_data in quizzes
        ]
        session.bulk_insert_mappings(QuizModel, data_list)
        session.commit()