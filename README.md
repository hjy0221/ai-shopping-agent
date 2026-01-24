# 🛍️ AI Smart Shopping Agent

> **"사용자의 추상적인 의도를 구체적인 상품 발견으로 연결하는 AI 에이전트"**

LLM(Google Gemini)의 추론 능력과 Naver Shopping API를 결합하여, **Context-Aware(맥락 인지) 검색**을 구현한 커머스 AI 프로젝트입니다. 기존 키워드 검색의 한계를 넘어, 대화형 인터페이스를 통해 탐색 비용을 줄이는 데 초점을 맞췄습니다.

🔗 **Live Demo:** [이곳을 클릭하여 바로 사용해보세요](https://ai-shopping-agent-a8vwz9eck8wybppcnlbfbd.streamlit.app/)
*(면접관님의 편의를 위해 Test API Key가 서버에 설정되어 있습니다. 별도 입력 없이 바로 테스트 가능합니다.)*

## 💡 Project Background & Motivation

**"힙한 친구 집들이 선물 추천해줘"**
커머스 플랫폼(무신사 등)에서 사용자는 종종 구체적인 상품명이 아닌 '상황'이나 '니즈'로 검색합니다. 하지만 기존 검색 엔진은 이러한 자연어 쿼리를 처리하기 어렵습니다.

저는 **AI Native Engineering** 관점에서 이 문제를 해결하고자 했습니다.
1. **Query Expansion:** LLM을 통해 추상적 질문을 구체적 상품 키워드로 변환합니다.
2. **Reasoning:** 단순 나열이 아닌, '왜 이 상품을 추천하는지'에 대한 설득(Tip)을 제공합니다.
3. **Responsive UX:** 모바일 트래픽이 높은 커머스 환경을 고려하여, 모바일 최적화 UI를 구현했습니다.

## ⚙️ Architecture & Tech Stack

![Architecture Diagram](https://mermaid.ink/img/pako:eNpVkMtqwzAQRX9FzKpF_AAXuBBCoS202WTRRh9rW4okaOQhjZHS_vcqaQpdjfTweM69M6PBKkWB4vaz_obW4wN9zB5e48d7x8vbr2-4vD_g9fN4R4v9o8KArf6Fw4F-09fO0p_5M33daQZ1i5bWqJp7hXbQ0lp01tJ68wY1rV-QJqgJPaE19A29o5_oI1qhi9A8x8_J4yOQS07qLzSp35A8k0sWSIl0w1wWUqL8XbI5k0zJjXJJS7L4s0iWkvk_i-M0L2XJ5D_2Bw2ST6c)

- **Core Logic:** `Python 3.10+`
- **LLM:** `Google Gemini Pro (gemini-1.5-flash)` - Query Analysis & Reasoning
- **Data Source:** `Naver Shopping API` - Real-time Product Data
- **Web Framework:** `Streamlit` - Interactive Web UI & Deployment

## 🚀 Key Features

1.  **Intelligent Query Processing**
    - 사용자의 자연어 질문을 분석하여 `Search Keywords`와 `Shopping Tips`로 구조화합니다.
    - 예: *"자취생 필수템"* → 키워드: *"규조토 발매트, 미니 밥솥"*, 팁: *"공간 차지가 적은 제품 위주로 선정했습니다."*

2.  **Hybrid User Experience**
    - **Chat Interface:** 대화하듯 편안한 검색 경험 제공.
    - **Visual Cards:** 상품 이미지, 가격, 구매 링크를 직관적인 카드 UI로 제공.

3.  **Cross-Platform Support**
    - PC 웹 환경은 물론, **모바일 환경**에서도 완벽하게 작동하는 반응형 디자인(Responsive Design)을 적용했습니다.
