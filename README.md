# AI Smart Shopping Interface

[日本語](https://github.com/hjy0221/ai-shopping-agent#%E6%97%A5%E6%9C%AC%E8%AA%9E) · [English](https://github.com/hjy0221/ai-shopping-agent#english) · [한국어](https://github.com/hjy0221/ai-shopping-agent#%ED%95%9C%EA%B5%AD%EC%96%B4)

[Live Demo](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)

## 日本語

Google Geminiの推論能力とネイバーショッピング検索APIを組み合わせて、自然言語の意図を商品ナビゲーションに結び付けるインタラクティブなショッピングインターフェースです。

### 主な機能

- 抽象的なリクエストを具体的な検索キーワードとショッピングのヒントに変換
- ネイバーショッピングのリアルタイム商品データを画像・価格・購入リンクカードで表示
- インタラクティブ検索とモバイル対応UI
- Streamlit Secretsまたはサイドバー入力によるAPIキーの設定

### 技術スタック

- Python、Streamlit
- Google Gemini
- Naver Shopping Search API

### を実行する

```bash
git clone https://github.com/hjy0221/ai-shopping-agent.git
cd ai-shopping-agent
pip install -r requirements.txt
streamlit run app_naver.py
```

アプリが開いたら、サイドバーにGoogle API Key、Naver Client ID、およびNaver Client Secretを入力します。キーをリポジトリにコミットしないでください。

## English

It is an interactive shopping interface that connects natural language intent to product exploration by combining Google Gemini's reasoning capabilities and Naver Shopping Search API.

### Main features

- Convert abstract requests into concrete search keywords and shopping tips
- Display real-time product data from Naver Shopping as image, price, and purchase link cards
- Interactive search and mobile-ready UI
- Set API keys via Streamlit Secrets or sidebar entry

### Technology Stack

- Python, Streamlit
-Google Gemini
- Naver Shopping Search API

### Run

```bash
git clone https://github.com/hjy0221/ai-shopping-agent.git
cd ai-shopping-agent
pip install -r requirements.txt
streamlit run app_naver.py
```

When the app opens, enter the Google API Key, Naver Client ID, and Naver Client Secret in the sidebar. Do not commit the key to the repository.

## 한국어

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
