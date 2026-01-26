import google.generativeai as genai

# 여기에 발급받은 API 키를 넣으세요
GOOGLE_API_KEY = "  "
genai.configure(api_key=GOOGLE_API_KEY)

print("내 API 키로 사용 가능한 모델 목록:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")