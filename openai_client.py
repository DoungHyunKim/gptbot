'''
OpenAI API 를 호출하여 GPT 응답을 생성합니다.
'''

import openai
import os
import json

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question: str, customer_data: dict):
    system_msg = f"당신은 {customer_data['company']}의 제품 설명 챗봇입니다."
    context_info = json.dumps(customer_data["products"], ensure_ascii=False)

    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"{question}\n\n제품 정보:\n{context_info}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.5
    )
    return response['choices'][0]['message']['content']