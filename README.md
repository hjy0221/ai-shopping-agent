# AI Smart Shopping Interface

[日本語](https://github.com/hjy0221/ai-shopping-agent#%E6%97%A5%E6%9C%AC%E8%AA%9E) · [English](https://github.com/hjy0221/ai-shopping-agent#english) · [한국어](https://github.com/hjy0221/ai-shopping-agent#%ED%95%9C%EA%B5%AD%EC%96%B4)

[Live Demo](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)

## 日本語

Google Gemini の推論と Naver Shopping Search API を組み合わせ、自然言語の要望から商品を探す対話型ショッピングインターフェースです。

### 主な機能

- 幅広い要望を具体的な検索キーワードと買い物のヒントに変換
- Naver Shopping の商品画像、価格、購入リンクをカードで表示
- モバイル対応の対話型検索
- Streamlit Secrets またはサイドバーで API 認証情報を設定

### 技術

Python、Streamlit、Google Gemini、Naver Shopping Search API。

### 実行方法

```bash
git clone https://github.com/hjy0221/ai-shopping-agent.git
cd ai-shopping-agent
pip install -r requirements.txt
streamlit run app_naver.py
```

起動後、サイドバーに Google API Key、Naver Client ID、Naver Client Secret を入力します。認証情報をリポジトリにコミットしないでください。

## English

An AI shopping interface that combines Google Gemini reasoning with the Naver Shopping Search API to turn natural-language intent into product discovery.

### Key features

- Converts broad requests into concrete search keywords and shopping tips
- Presents live Naver Shopping results as cards with images, prices, and purchase links
- Provides a conversational, mobile-friendly search experience
- Accepts API credentials through Streamlit Secrets or sidebar inputs

### Tech stack

- Python and Streamlit
- Google Gemini
- Naver Shopping Search API

### Run locally

```bash
git clone https://github.com/hjy0221/ai-shopping-agent.git
cd ai-shopping-agent
pip install -r requirements.txt
streamlit run app_naver.py
```

When the app opens, enter your Google API Key, Naver Client ID, and Naver Client Secret in the sidebar. Never commit credentials to the repository.

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
