from typing import Union, Any, List, Dict
from fastapi import FastAPI
from cachetools import LRUCache
from httpx import Client

from app.schemas import QuestionRequest
from app.services import add_quiz_data_in_db

app = FastAPI()
cache = LRUCache(maxsize=1)


@app.post('/question/')
def question(request_data: QuestionRequest) -> Union[List[Dict[str, Any]], None]:
    with Client() as client:
        response_jservice = client.get(f'https://jservice.io/api/random?count={request_data.questions_num}')
    
    quizzes = response_jservice.json()
    response = cache.get('previous_response')

    if response_jservice.status_code == 200:
        cache['previous_response'] = quizzes
        add_quiz_data_in_db(quizzes=quizzes)

    return response