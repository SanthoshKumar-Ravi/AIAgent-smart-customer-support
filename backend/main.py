from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
from uuid import uuid4
from feedback import store_feedback
from model import get_qa_chain

app = FastAPI()
redis = Redis(host="localhost", port=6379, decode_responses=True)
qa_chain = get_qa_chain()

class Query(BaseModel):
    question: str

class Feedback(BaseModel):
    query_id: str
    rating: int
    comment: str

@app.post("/query/")
def handle_query(query: Query):
    query_id = str(uuid4())
    redis.hset(query_id, mapping={"question": query.question})

    try:
        answer = qa_chain.run(query.question)
    except Exception as e:
        answer = f"Error generating answer: {str(e)}"

    redis.hset(query_id, "answer", answer)
    return {"query_id": query_id, "answer": answer}

@app.post("/feedback/")
def submit_feedback(feedback: Feedback):
    store_feedback(redis, feedback)
    return {"message": "r recorded."}
