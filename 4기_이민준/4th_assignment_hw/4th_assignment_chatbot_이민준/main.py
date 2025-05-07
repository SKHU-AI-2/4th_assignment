import os
print(f"[DEBUG] OPENWEATHER_API_KEY = {os.getenv('OPENWEATHER_API_KEY')}")

from api.weather import get_weather

def chat():
    print("🌤️ 날씨 챗봇입니다. 도시 이름을 입력하세요. 종료하려면 '종료'라고 입력하세요.")
    while True:
        city = input(">> ")
        if city.strip().lower() == "종료":
            print("챗봇을 종료합니다.")
            break
        try:
            result = get_weather(city)
            print("✅", result)
        except Exception as e:
            print("⚠️ 에러:", e)

if __name__ == "__main__":
    chat()
