'''
FastAPI 서버로, /chat 엔드포인트를 통해 질문을 처리합니다.
'''

from fastapi import FastAPI, Request
import json
from openai_client import ask_gpt

app = FastAPI()

def load_customer_data(client_id: str):
    try:
        with open(f'customer_data/{client_id}.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question")
    client_id = request.query_params.get("client_id")

    customer_data = load_customer_data(client_id)
    if not customer_data:
        return {"error": "Unknown client_id"}

    response = ask_gpt(question, customer_data)
    return {"answer": response}