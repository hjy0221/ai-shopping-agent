# AI Smart Shopping Interface

[日本語](README.ja.md) · [English](README.md) · [한국어](README.ko.md)

[Live Demo](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)

Google Gemini의 추론 능력과 네이버 쇼핑 검색 API를 결합해 자연어 의도를 상품 탐색으로 연결하는 대화형 쇼핑 인터페이스입니다.

### 주요 기능

- 추상적인 요청을 구체적인 검색 키워드와 쇼핑 팁으로 변환
- 네이버 쇼핑의 실시간 상품 데이터를 이미지·가격·구매 링크 카드로 표시
- 대화형 검색과 모바일 대응 UI
- Streamlit Secrets 또는 사이드바 입력을 통한 API 키 설정

### 기술 스택

- Python, Streamlit
- Google Gemini
- Naver Shopping Search API

### 실행하기

```bash
git clone https://github.com/hjy0221/ai-shopping-agent.git
cd ai-shopping-agent
pip install -r requirements.txt
streamlit run app_naver.py
```

앱이 열리면 사이드바에 Google API Key, Naver Client ID, Naver Client Secret을 입력합니다. 키를 저장소에 커밋하지 마세요.
