import os
from dotenv import load_dotenv
import google.generativeai as genai

def ai_researcher_prompt(query):
    """AI 연구자 역할을 수행하는 프롬프트 생성"""
    prompt = f"""당신은 인공지능(AI) 분야의 전문 연구자입니다.
사용자의 질문에 대해 깊이 있는 분석과 최신 정보를 바탕으로 답변해야 합니다.
답변은 명확하고 간결하며, 필요한 경우 관련 연구 자료나 기술 동향을 언급할 수 있습니다.

질문: {query}

답변:"""
    return prompt

def main():
    # .env 파일에서 환경 변수 로드
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Gemini API 키가 있는지 확인
    if not GEMINI_API_KEY:
        print("GEMINI_API_KEY가 .env 파일에 설정되지 않았습니다.")
        return

    # GeminiPro 모델 설정
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat()
    except Exception as e:
        print(f"Gemini API 설정 오류: {e}")
        print("API 키를 확인하거나 네트워크 상태를 확인해주세요.")
        return

    print("AI 연구자 챗봇을 시작합니다. '종료'를 입력하면 종료됩니다.")

    while True:
        user_input = input("연구 질문: ")
        if user_input.lower() == '종료':
            print("챗봇을 종료합니다.")
            break

        try:
            # AI 연구자 프롬프트 생성
            prompt = ai_researcher_prompt(user_input)
            response = chat.send_message(prompt)
            print("AI 연구자:", response.text)
        except Exception as e:
            print(f"오류 발생: {e}")
            print("API 요청 중 오류가 발생했습니다. 네트워크 상태를 확인해주세요.")

if __name__ == "__main__":
    main()