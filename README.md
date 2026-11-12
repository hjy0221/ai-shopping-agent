# AI Smart Shopping Interface

[日本語](README.ja.md) · [English](README.md) · [한국어](README.ko.md)

[Live Demo](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)

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
