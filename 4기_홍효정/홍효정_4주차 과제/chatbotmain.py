import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.environ['API_KEY']
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

MODEL = 'gpt-4'  # 또는 'gpt-3.5-turbo'
client = OpenAI(api_key=API_KEY)  # base_url 제거

messages = [
    {'role': 'system', 'content': SYSTEM_MESSAGE}
]

print('챗봇을 시작합니다! (종료하려면 "exit" 또는 "quit"입력)')

while True:
    user_input = input("You : ")
    if user_input.lower() in ['exit', 'quit']:
        print("챗봇을 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )

    chatbot_reply = response.choices[0].message.content
    print("Chatbot : ", chatbot_reply)

    messages.append({"role": "assistant", "content": chatbot_reply})
