from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["GROQ_API_KEY"]
BASE_URL = "https://api.groq.com/openai/v1"
MODEL = "llama3-8b-8192"  # or "llama3-70b-8192"
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

messages = [
    {
        'role': 'system',
        'content': SYSTEM_MESSAGE
    }
]

print("챗봇을 시작합니다. 종료하려면 quit 또는 exit를 입력하세요.")

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit"]:
        print("챗봇을 종료합니다.")
        break

    messages.append({'role': 'user', 'content': user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    print(f"Chatbot: {reply}")

    messages.append({'role': 'assistant', 'content': reply})
