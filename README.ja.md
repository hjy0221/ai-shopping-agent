# AI Smart Shopping Interface

[日本語](README.ja.md) · [English](README.md) · [한국어](README.ko.md)

[Live Demo](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)

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
